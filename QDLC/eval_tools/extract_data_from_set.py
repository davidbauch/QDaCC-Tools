def extract_single_dataset(set_filetosort: str, destiny: str, extraction_modes: str | tuple[str] = "auto", filesize_threshold: float = 100*1024*1024, set_of_filters: dict = {}, interpolate: bool = False, interpolation_points: int = 500, print=print):
    """Extracts data from a single dataset and returns a list of dictionaries with the data to plot
    
    Args:
        set_filetosort (str): Path to the file to sort
        destiny (str): Path to the folder to evaluate
        extraction_modes (str, optional): Extraction mode. Defaults to "auto".
        filesize_threshold (float, optional): Filesize threshold in MB. Defaults to 100*1024*1024.
        set_of_filters (dict, optional): Set of filters to apply. Defaults to {}.
        interpolate (bool, optional): Interpolate the data. Defaults to False."""
    
    """
    extraction modes:
    - set_of_calculations_to_endpoint - Gathers the endpoints of a set of calculations and stores it using line syntax
    - set_of_calculations_to_matrix - Gathers the last line of a set of calculations and stores it using a matrix syntax
    - set_of_calculations_to_endpoint_matrix - Gathers the endpoints of a set of calculations and stores it using a matrix syntax
    
    - interpolate - Interpolattion of the data to X number of points
    filter:
    - norm - Purge of the data to remove outliers
    - nan - Purge of the data to remove NaNs
    - max,median,average - Apply custom filter to the last N data points and use the filters final value instead of [-1]
    """
    import os
    from random import choice
    from QDLC.misc.functionality import (_get_files_to_sort, 
        _get_folders_to_evaluate, 
        _get_logfile_index, 
        _guess_delimiter, 
        _generate_data_lines,
        _get_data_header,
        _final_point_filter,
        _matrix_filter,
        _interpolate_data,
        _clean_data,
        _guess_file_lines,
        _guess_extraction_mode)
    
    from QDLC.misc.terminal_colors import RESET, BOLD, GREY, RED, YELLOW, GREEN


    # Normalize Path:
    destiny = os.path.normpath(destiny)
    
    # Target Filetype
    target_filetype = ".txt"

    # File Delimiter of the output files. Always normalize to " "
    file_delimiter = None
    output_delimiter = " "

    print(f"Evaluating '{GREY}{destiny}{RESET}'")

    # Generate target folder for evaluated data.
    output_path = os.path.join(destiny,"img")
    os.makedirs( output_path, exist_ok=True )
    print(f"Output path is '{GREY}{output_path}{RESET}'")
    
    # Gather all folders to evaluate
    all_folders = sorted(_get_folders_to_evaluate(destiny, filter = ["img"]))

    # Path to exemplary folder
    first_folder = choice(all_folders)

    # Gather all files to sort
    files_to_sort = []
    if (set_filetosort == "all"):
        # Look into destiny folder and evaulate all .txt files. Maybe check for filesize so G1 and G2 matrices are excluded
        print(f"Looking for files to evaluate that are {YELLOW}smaller than {filesize_threshold/1024/1024} MB{RESET}.")
        files_to_sort = _get_files_to_sort(os.path.join(destiny,first_folder), filesize_threshold, filter = ["logfile.log", "settings_"])
    else:
        files_to_sort.extend(set_filetosort.split(","))
    print("Evaluating the following files:")
    [print(f" - {GREY}{file}{RESET}") for file in files_to_sort]

    # Path to first files
    path_to_first_file = os.path.join(destiny,first_folder,files_to_sort[0])
    path_to_first_logfile = os.path.join(destiny,first_folder,"logfile.log")
    
    # Cache succesfully eavaluated files
    evaluated_files = []


    if extraction_modes == "auto":
        extraction_modes = _guess_extraction_mode(path_to_first_logfile)
        print(f"Extraction method was guessed to be '{GREY}{', '.join(extraction_modes)}{RESET}' using '{GREY}{path_to_first_logfile}{RESET}'")
    if not isinstance(extraction_modes, tuple):
        extraction_modes = (extraction_modes,)

    # Guess file_delimiter
    if file_delimiter is None:
        file_delimiter = _guess_delimiter(path_to_first_file)
        print(f"The file_delimiter was guessed to be '{GREY}{file_delimiter}{RESET}' using '{GREY}{os.path.join(destiny,first_folder,files_to_sort[0])}{RESET}'")

    for extraction_mode in extraction_modes:
        # Output prefix is defined by the extraction mode. Each extraction mode has its own output format.
        fileout_prefix = "out_endpoints_"
        if extraction_mode == "set_of_calculations_to_matrix":
            fileout_prefix = "out_"
        elif extraction_mode == "set_of_calculations_to_endpoint":
            fileout_prefix = "endpoints_"
        print(f"Current Extraction method is '{GREY}{extraction_mode}{RESET}'. File format will be '{GREY}{fileout_prefix}file{target_filetype}{RESET}'")


        # Inform about interpolation
        if (interpolate):
            if extraction_mode != "set_of_calculations_to_matrix":
                print(f"{YELLOW}Interpolation{RESET} is {RED}{BOLD}not{RESET} supported for this extraction mode. Disabling interpolation.")
                interpolate = False
            else:
                approximated_filelines = _guess_file_lines(path_to_first_file)
                saved_lines = interpolation_points / approximated_filelines
                print(f"{YELLOW}Interpolation{RESET} is {GREEN}{BOLD}enabled{RESET}. Interpolating to {interpolation_points} points. Approx. {saved_lines*100:.2f}% of initial data points.")

        for current_output_file in files_to_sort:
            print(f"Evaluating '{GREY}{current_output_file}{RESET}'...")
            current_output_file_no_extension = "".join(current_output_file.split(".")[:-1])
            # Open current file in each folder and append its content to list, depending on extraction mode
            current_content = []
            for current_folder in all_folders:
                path_to_current_file = os.path.join(destiny,current_folder,current_output_file)
                try:
                    logfile_index = _get_logfile_index(os.path.join(destiny,current_folder,"logfile.log"))
                except FileNotFoundError:
                    print(f"{RED}Folder '{current_folder}' could not be evaluated!{RESET} Logfile not found!")
                    continue
                except AttributeError:
                    print(f"{RED}Folder '{current_folder}' could not be evaluated!{RESET} Logfile does not contain the necessary indices!")
                    continue
                try:
                    data = open(path_to_current_file, "r").readlines()[1:]
                except FileNotFoundError:
                    print(f"{RED}File '{path_to_current_file}' does not exist!{RESET}")
                    continue
                data = _clean_data(data, file_delimiter, output_delimiter)
                
                # Filters that leave the column dimension can be applied in all modes
                for filter in [matrix_filter for matrix_filter in set_of_filters.values() if matrix_filter["type"] == "matrix"]:
                    data = _matrix_filter(data, filter["function"], replacement=filter["replacement"],delimiter=output_delimiter)
                
                # Apply Reduction Filters when in endpoint mode.
                if extraction_mode != "set_of_calculations_to_matrix":
                    for filter in [endpoint_filter for endpoint_filter in set_of_filters.values() if endpoint_filter["type"] == "endpoint"]:
                        data = _final_point_filter(data, filter["function"], delimiter=output_delimiter)
               
                
                # Interpolate Data if necessary. TODO: interpolate to max X
                if interpolate:
                    data = _interpolate_data(data, index = 0, points = interpolation_points, delimiter=output_delimiter)
                # Add logfile index to each line
                data = _generate_data_lines(logfile_index, data, output_delimiter)
                # Append data to current content
                current_content.extend( data )
        
            # Sort output after logfile indices and first data column
            current_content = sorted(current_content, key = lambda x: (float(x.split(output_delimiter)[0]), float(x.split(output_delimiter)[1])))
            
                
            # Create output file path
            current_output_file_path = os.path.join(destiny,"img",fileout_prefix+current_output_file_no_extension+target_filetype)
            
            # Create output file
            with open(current_output_file_path, "w") as out:
                # Use the last current file to extract a header line
                path_to_any_of_current_files = os.path.join(destiny,first_folder,current_output_file)
                data_header = _get_data_header(path_to_any_of_current_files, file_delimiter, output_delimiter)
                # Extend the data header at the front with logfile counter indices to match the lenght of a dataline
                #header_extensions = len(current_content[0].split(output_delimiter))-len(data_header.split(output_delimiter))
                #data_header = output_delimiter.join([f"lfc{i}" for i in range(header_extensions)] + [data_header])
                # Write header line
                print(data_header, file = out)
                # Write content. If mode is set_of_calculations_to_matrix, add empty line after each dataset.
                last_line_index = current_content[0].split(output_delimiter)[0]
                for line in current_content:
                    if extraction_mode == "set_of_calculations_to_matrix" or extraction_mode == "set_of_calculations_to_endpoint_matrix":
                        current_line_index = line.split(output_delimiter)[0]
                        if last_line_index != current_line_index:
                            print("", file = out)
                            last_line_index = current_line_index
                    print(line, file = out)
            
            # Cache filepath
            evaluated_files.append({"Path" : current_output_file_path, "extraction_method" : extraction_mode})
            
    return evaluated_files

if __name__ == "__main__":
    print("This file is part of the QDLC evaluation framework and should not be executed on its own.")