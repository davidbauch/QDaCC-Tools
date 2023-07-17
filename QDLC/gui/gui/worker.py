from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QTextBrowser
from subprocess import Popen, PIPE
from .parse_ansi import replace_ansi_escape_sequences
from os import environ
from numpy import array as to_np_array

class QDaCCThread(QThread):
    finished = Signal()
    progress = Signal(str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__()
        self.parent = parent
        self.finished.connect(self.deleteLater)
        self.finished.connect(self.quit)
        self.running = False
        self.cwd = kwargs.pop("cwd", None)
        self.args = args
        self.kwargs = kwargs

    def connectStarted(self, function):
        self.started.connect(function)
        return self
    def connectProgress(self, function):
        self.progress.connect(function)
        return self
    def connectFinished(self, function):
        self.finished.connect(function)
        return self

    def pipeUpdatesTo(self, field_update_function, progressbar_update_function = None):
        def update(text: str):
            if len(text) == 0 or text == " ":
                return
            if "%" in text:
                if progressbar_update_function is None:
                    return
                percent = text.split("%")[0].split()[-1]
                progressbar_update_function(int(float(percent)))
                return
            field_update_function(text)
        self.connectProgress(update)
        return self
    
    def runExternal(self, command: str | list[str]):
        if not isinstance(command, list):
            command = self.parent.commandToCLAList(command, escape_symbol="")
        print(f"Running QDaCC Worker with command {command}...")
        print(f"Executable directory is {self.cwd}")
        self.running = True
        env = environ.copy()
        env["PYTHONUNBUFFERED"] = "1"
        self.process = Popen(command, stdout=PIPE, universal_newlines = True, cwd=self.cwd, shell=True, env=env)
        while self.running:
            output = self.process.stdout.readline()
            if output == '' and self.process.poll() is not None:
                break
            self.progress.emit(replace_ansi_escape_sequences(output.strip()))
        self.process.communicate()
    
    def stop(self):
        self.running = False
        self.finished.emit()
        self.quit()
    

class QDaCCMainWoker(QDaCCThread):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
    def run(self):
        if "command" in self.kwargs:
            self.runExternal(self.kwargs["command"])
        else: raise Exception("No command specified for QDaCCMainWorker")

class QDaCCSettingGenerator(QDaCCThread):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
    def run(self):
        if not "mgx" in self.kwargs or not "mgy" in self.kwargs or not "values" in self.kwargs:
            raise Exception("No inputs specified for QDaCCSettingGenerator")
        if not "file" in self.kwargs or not "name" in self.kwargs:
            raise Exception("No file specified for QDaCCSettingGenerator")
        if not "converter" in self.kwargs:
            raise Exception("No converter specified for QDaCCSettingGenerator")
        mgx, mgy, values = self.kwargs["mgx"], self.kwargs["mgy"], self.kwargs["values"]
        output_file, name, converter = self.kwargs["file"], self.kwargs["name"], self.kwargs["converter"]
        runstring = self.kwargs["runstring"]
        one, two = self.kwargs["one"], self.kwargs["two"]
        with open(output_file, "w") as f:
            f.write(f"# {name}\n")
            self.progress.emit(f"# {name}")
            if one:
                for i,j in [(i,j) for i in range(mgx.shape[0]) for j in range(mgx.shape[1])]:
                    x1,x2 = mgx[i,j],mgy[i,j]
                    format_dict = {name.split("(",1)[0] : values[i,j] for name,values in values.items()}
                    if two:
                        runstr = converter(runstring.replace("[QDaCC]", f"QDaCC --lfc {x1},{x2}").replace("[FILEPATH]",""))
                        runstr = " ".join(runstr)
                        f.write(f"{runstr.format(**format_dict)}\n")
                    else:
                        runstr = converter(runstring.replace("[QDaCC]", f"QDaCC --lfc {x1}").replace("[FILEPATH]",""))
                        runstr = " ".join(runstr)
                        f.write(f"{runstr.format(**format_dict)}\n")
                    self.progress.emit(f"{100*(i*mgx.shape[0] + j)/mgx.shape[0]/mgx.shape[1]}%")
                self.progress.emit(f"Saved {mgx.shape[0]*mgx.shape[1]} settings to {output_file}")
            else:
                runstr = converter(runstring.replace("[QDaCC]", "QDaCC").replace("[FILEPATH]",""))
                self.progress.emit(f"Saved 1 setting1 to {output_file}")
                f.write(f"{runstr}\n")
        
        self.progress.emit("Done")
        self.finished.emit()

from os.path import join
from scipy.optimize import minimize
from numpy import ndarray

class QDaCCOptimizer(QDaCCThread):
    plot_hint = Signal()
    outset = Signal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cwd = kwargs.pop("cwd", None)
        self.data = []
        self.quality_data = []
        self.parameter_data = [[] for _ in kwargs["initial_parameters"]]
        self.current_parameters = []
        self.current_iteration = 0
        self.maximum_cached_data = 5
        self.eval_dict = kwargs.pop("base_eval_dict", {})
        self.variables = kwargs.pop("variables", {})
        self.variables_to_plot = []
        self.eval_dict.update({f"V{i}" : p for i,(k,p) in enumerate(self.variables.items(),1)})
        self.eval_dict.update({"last" : lambda x: x[-1] if isinstance(x, list) else x})
        self.runstring = ""
        self.brute_force_kill = False
        self.plot_after_iteration = kwargs.pop("plot_after_iteration", False)
        self.plot_is_folder = kwargs.pop("plot_is_folder", False)
        self.path = kwargs.pop("path", "")
        self.parent = kwargs.pop("parent", None)

    def readFiles(self, path: str, files: list[str], indices: list[list[int]]) -> list[tuple]:
        data = []
        for file, index in zip(files, indices):
            with open(join(path,file),"r") as f:
                print(f"Reading {file} with indices {index}")
                content = f.readlines()[1:]
                content_transposed = list(zip(*[[float(a) for a in line.split()] for line in content if len(line) and not line.startswith("\n")]))
                x = content_transposed[0]
                #for col in content_transposed[1:]:
                for ind in index:
                    data.append( (x,content_transposed[ind]) )
                
        print(f"Read {len(data)} files")
        return data
        
    def evaluate(self, params: list[float]):
        if self.brute_force_kill:
            self.kill()
        self.current_parameters = params
        self.eval_dict.update({f"P{i}" : p for i,p in enumerate(self.current_parameters,1)})
        # Update Variables
        self.variables_to_plot.clear()
        for i,(k,p) in enumerate(self.variables.items(),1):
            try:
                self.eval_dict[f"V{i}"] = eval(p, self.eval_dict) if p != "" else ""
            except Exception as e:
                self.eval_dict[f"V{i}"] = ""

            if isinstance(self.eval_dict[f"V{i}"], (list,tuple,ndarray)) and len(self.data)>0 and len(self.eval_dict[f"V{i}"]) == len(self.data[0][0][0]):
                self.variables_to_plot.append(self.eval_dict[f"V{i}"])
        
        # Format Settingfile if required
        if self.plot_is_folder:
            # Get Path in runstring
            settingfile = self.parent.textinput_path_to_settingfile.text()
            new_content = []
            with open(settingfile, "r") as f:
                content = f.readlines()
                new_content = [content[0]]
                # Replace Each line with the eval'ed runstring
                for line in content[1:]:
                    self.eval_dict["basestring"] = line
                    new_content.append( eval(self.kwargs["formatter"], self.eval_dict) )
            with open(settingfile, "w") as f:
                f.writelines(new_content)
        
        # Set/Reset Basestring to command
        self.eval_dict.update({"basestring" : self.kwargs["command"], "parameters" : self.current_parameters})
        # Format Runstring
        self.runstring = eval(self.kwargs["formatter"], self.eval_dict)
        print(f"Calculating {self.runstring}")
        self.outset.emit(f"Calculating {self.current_parameters}")
        
        # Run QDaCC
        self.runExternal(self.runstring)

        # Unformat Settingfile if required
        if self.plot_is_folder:
            with open(settingfile, "w") as f:
                f.writelines(content)

        # Plot Results if required
        if self.plot_after_iteration:
            plot_command = ["python3", "-m", "QDLC.eval_tools.get_files", "all", self.path,"-folder" if self.plot_is_folder else "", "--type=png(50)"]
            # Call plot command
            self.runExternal(plot_command)

        data = self.readFiles(self.kwargs["path"], self.kwargs["files"], self.kwargs["indices"])
        
        self.eval_dict.update({f"Y{i}" : to_np_array(p[1]) for i,p in enumerate(data,1)}) 
        # Evaluate Fitness Function
        quality = eval(self.kwargs["fitness"], self.eval_dict)

        # Append to lists
        self.data.append(data)
        if len(self.data) > self.maximum_cached_data:
            self.data.pop(0)

        self.quality_data.append(quality)
        for i,p in enumerate(self.current_parameters):
            self.parameter_data[i].append(p)
        return quality
    
    def callback(self, current_parameters):
        if self.brute_force_kill:
            self.kill()
        print(f"Current quality value is {self.quality_data[-1]}")
        self.outset.emit(f"{self.current_iteration}: Current parameters are {current_parameters}, current Fitness is {self.quality_data[-1]}")

        if self.current_iteration % 1 == 0:
            self.plot_hint.emit()
        self.current_iteration += 1

    def outputParametersTo(self, field: QTextBrowser):
        self.outset.connect(lambda x: field.append(x))

    def run(self):
        if "command" not in self.kwargs:
            self.outset.emit("No command specified for QDaCCOptimizer")
        runstring = self.kwargs["command"]
        if not "{" in runstring or not "}" in runstring:
            self.outset.emit("No parameter in runstring for QDaCCOptimizer")
            if self.plot_is_folder:
                self.outset.emit("But the Optimizer will evaluate the setting file, so this may be intended.")


        res = minimize(self.evaluate, self.kwargs["initial_parameters"], method='nelder-mead',options={'xatol': float(self.kwargs["tol"]), 'disp': True, 'maxiter': int(self.kwargs["maxit"])}, tol=self.kwargs["tol"], bounds=self.kwargs["bounds"], callback=self.callback) #nelder-mead, BFGS

        self.progress.emit(f"Finished optimization with result {res}")
        self.outset.emit(f"Final parameters are {self.current_parameters}, Final Fitness is {self.quality_data[-1]}")
        self.finished.emit()

    def kill(self):
        self.stop()
        raise Exception("Buretforce kill.")