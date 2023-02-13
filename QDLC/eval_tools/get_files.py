"""
This interactive script is used to extract data from QDLC simulation.
"""

if __name__ == "__main__":
    import sys, os

    from QDLC.misc.generate_colormaps import generate_colormaps
    from QDLC.plot_tools.general_matrix_plot import plot_matrix
    from QDLC.eval_tools.extract_data_from_set import extract_single_dataset

    # Help
    if (len(sys.argv) < 3 or any([a in sys.argv for a in ["-h","--help"]])):
        print("# Need at least 2 input arguments: FileToSort, Destiny")
        print("############################## Evaluation Parameters #####################################################################")
        print("#   -m, -e, -em            --  Extraction mode matrix, entpoint, endpoint_matrix. Can be combined.")
        print("#   --local=min:max        --  Use a local interval and gather the maximum value of this interval instead of using [-1]")
        print("#   -maxima                --  Uses the max() function on the datasets")
        print("#   --purge=min:max        --  Ignores all values outside the interval min:max")
        print("#   -purgeNAN              --  Purge NaN values from the dataset")
        print("#   --offset=int           --  Use [-offset] instead of [-1] for the final datapoints of the dataset")
        print("#   --last=int             --  Use [-offset-last:] instead of [-1] for the final datapoints of the dataset")
        print("############################## Processing Parameters #####################################################################")
        print("#   -folder                --  Evaluates this script in the entire folder, treating every subfolder as a complete dateset")
        print("#   -interpolate           --  Interpolates the dataset onto 500 points")
        print("############################## Plotting Parameters #######################################################################")
        print("#   --colormap=str         --  Colormap for plots. Default is 'turbo'")
        #print("#   --delim=str            --  Delimitor for plots. Default is ' '")
        print("#   -cbs                   --  Plot a single colorbar for all plots. Otherwise, a colorbar for every plot is used.")
        #print("#   -forceSingle           --  Force use of only one of the logfile counters.")
        print("# Note that this script will REQUIRE the logfilecounter to be present for sorting.")
        exit()

    # Input Parameters
    set_filetosort = str(sys.argv[1])
    
    destiny = os.path.normpath(sys.argv[2])

    # Redundant due to --last and --offset
    local = None
    if any(["--local=" in a for a in sys.argv]):
        local = [[b for b in a.replace("--local=","").split(":")] for a in sys.argv if "--local=" in a][0]
        local = [ float(a) if "." in a or "E" in a or "e" in a else int(a) for a in local]
        print("Looking for 'endpoint' as a local maxima in interval {}".format(local))
    
    purge = None
    if any(["--purge=" in a for a in sys.argv]):
        purge = [[float(b) for b in a.replace("--purge=","").split(":")] for a in sys.argv if "--purge=" in a][0]
        print(f"Purging all values outside of [{purge[0]},{purge[1]}]")
    
    clear_nans = "-purgeNAN" in sys.argv
    
    endpoint_shift = [int(a.split("=")[-1]) for a in sys.argv if "--offset" in a.split("=")][0] if any( ["--offset" in a.split("=") for a in sys.argv] ) else 0 # The endpoint chosen will shift by this amount
    endpoint_num = [int(a.split("=")[-1]) for a in sys.argv if "--last" in a.split("=")][0] if any( ["--last" in a.split("=") for a in sys.argv] ) else 0 # This number of endpoints will be chosen
    
    interpolate = "-interpolate" in sys.argv
    
    # Plotting Parameters
    use_cbs = "-cbs" in sys.argv
    colormap = [a.replace("--colormap=","") for a in sys.argv if "--colormap=" in a ][0] if any(["--colormap=" in a for a in sys.argv]) else "turbo"
    
    # Folder evaluation
    use_folder = "-folder" in sys.argv
    
    # Input Extraction Mode
    extraction_modes = []
    if "-m" in sys.argv:
        extraction_modes.append("set_of_calculations_to_matrix")
    if "-e" in sys.argv:
        extraction_modes.append("set_of_calculations_to_endpoints")
    if "-em" in sys.argv:
        extraction_modes.append("set_of_calculations_to_endpoints_matrix")
    if len(extraction_modes) > 0:
        extraction_modes = tuple(extraction_modes)
    else:
        extraction_modes = "auto"
    # Filesize threshold in MB
    filesize_threshold = 100*1024*1024 # 100 MB

    evaluated_files = []
    if use_folder:
        from QDLC.misc.functionality import _get_folders_to_evaluate
        print(f"Evaluating all folders in {destiny}")
        folders = [os.path.join(destiny, folder) for folder in _get_folders_to_evaluate(destiny, filter = ["img"])]
    else:
        folders = [destiny]

    # Create Filter:
    filter = {}
    if any(["endpoint" in el for el in extraction_modes]) or extraction_modes == "auto":
        end = None if endpoint_shift == 0 else endpoint_shift - 1
        filter["endpoints"] = {"type": "endpoint", "function": lambda x: x[-1-endpoint_shift-endpoint_num:end]}
    if purge is not None:
        filter["norm_down"] = {"type": "matrix", "function": lambda x: float(x) < purge[0], "replacement" : lambda x: "nan" }
        filter["norm_up"] = {"type": "matrix", "function": lambda x: float(x) > purge[1], "replacement" : lambda x: "nan"}
    if clear_nans:
        filter["nan"] = {"type": "matrix", "function": lambda x: x in ["nan", "NaN", "NAN"], "replacement": None}
    if "-maxima" in sys.argv:
        filter["max"] = {"type": "endpoint", "function": lambda x: f"{max([float(v) for v in x[-1-endpoint_shift-endpoint_num:end]])}"}
        
    
    print("Filters applyed if possible:")
    [print(f" - {a}") for a in filter.keys()]

    # Evaluate
    for destiny in folders:
        # Check if there is a logfile in folder. If no, evaluate folder, if yes, add files in folder to plot
        folder_content = os.listdir(destiny)
        if "logfile.log" in folder_content:
            print(f"Found logfile in {destiny}. Plotting files in folder.")
            from QDLC.misc.functionality import _get_files_to_sort
            new_files = _get_files_to_sort(destiny, filesize_threshold, filter = ["logfile.log", "settings_"])
            new_files = [ {"Path": os.path.join(destiny, file), "extraction_method": "line"} for file in new_files ]
        else:
            new_files = extract_single_dataset(set_filetosort, destiny, extraction_modes=extraction_modes, filesize_threshold=filesize_threshold, interpolate=interpolate, set_of_filters=filter)
        evaluated_files.extend(new_files)

    # Plotting
    print(f"Plotting {len(evaluated_files)} files")
    for file in evaluated_files:
        current_output_file_path = file["Path"]
        plot_type = "matrix" if "matrix" in file["extraction_method"] else "line"
        try:
            plot_matrix(current_output_file_path, mode=plot_type)
        except Exception as e:
            print(f"Error while plotting matrix: {e}")