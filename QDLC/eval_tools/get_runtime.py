"""
This interactive script is used to extract the runtime from QDLC simulations.
"""

def time_to_str(time):
    """
    Converts a time string to a string and a float.
    :param time: Time string.
    :return: String.
    """
    if time == "--":
        return 0, 0
    ret = ""
    for entry in time.split(":"):
        if not "ms" in entry:
            ret += entry
    h,m,s,ms = "0","0","0","0"
    if "h" in ret:
        h = ret.split("h")[0]
        ret = ret.split("h")[1]
    if "m" in ret:
        m = ret.split("m")[0]
        ret = ret.split("m")[1]
    if "s" in ret:
        s = ret.split("s")[0]
    if "ms" in time:
        ms = time.split("ms")[0].split(":")[-1]
        if any([a in ms for a in ["h","m","s"]]):
            ms = 0
    seconds = 60*60*int(h) + 60*int(m) + int(s)
    milliseconds = float(seconds)*1000 + float(ms)
    return f"{time.replace(':','')} {str(milliseconds)}"

def get_runtime(path: str, output_path: str | None = None, keys: list[str] | None = None):
    import os
    from QDLC.misc.functionality import _get_folders_to_evaluate, _get_logfile_index
    from parse import parse

    # Output Data
    output = []
    header = None

    # Gather all folders to evaluate
    all_folders = sorted(_get_folders_to_evaluate(path, filter = ["img"]))

    # Get Time lines of Logfiles
    for current_folder in all_folders:
        # Path to Logfile
        path_to_current_file = os.path.join(path,current_folder,"logfile.log")
        # Get Logfile Index
        logfile_index = _get_logfile_index(path_to_current_file)
        # Read Logfile
        data = open(path_to_current_file, "r").readlines()
        # Get Time lines
        time_lines = [ parse("{name}: Walltime: {walltime} CPUTime: {cputime}{trash}", l) for l in data if "Walltime" in l if (keys is None or any([key in l for key in keys])) ]
        # Add to Output
        if header is None:
            header = " ".join( [f"Walltime({el['name'].strip()}) CPUTime({el['name'].strip()}) Seconds(Walltime({el['name'].strip()})) Seconds(CPUTime({el['name'].strip()}))" for el in time_lines] )
        output.append(f"{logfile_index[0]} " + " ".join( [ f"{time_to_str(el['walltime'])} {time_to_str(el['cputime'])}" for el in time_lines] ))
    
    # Save to output file
    output.sort(key = lambda entry : float(entry.split(" ")[0]))
    if output_path is None:
        output_path = os.path.join(path, "time.txt")
    print(f"Saving to {output_path}")
    with open(output_path, "w") as f:
        print(header, file=f)
        for line in output:
            print(line, file=f) 

if __name__ == "__main__":
    from sys import argv
    get_runtime( argv[1] )