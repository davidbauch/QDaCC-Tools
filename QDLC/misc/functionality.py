
def _get_files_to_sort(path: str, filesize_threshold: float, filter: list[str]) -> list[str]:
    """
    Returns a list of files to sort.
    :param path: Path to the folder containing the files to sort.
    :param filesize_threshold: Threshold for the filesize of the files to sort. Larger files will be ignored.
    :param filter: List of files to ignore.
    :return: List of files to sort.
    """
    from os import walk
    from os.path import join, getsize
    # Get Set of unique files
    for root,_,files in walk(path):
        found = [f for f in files if f not in filter and not any([f.startswith(k) for k in filter]) and f.endswith(".txt") and getsize(join(root,f)) < filesize_threshold]
        unique_files_to_evaluate = sorted(list(set(found)))
        return unique_files_to_evaluate

def _get_folders_to_evaluate(path: str, filter: list[str]) -> list[str]:
    """
    Returns a list of folders to evaluate.
    :param path: Path to the folder containing the folders to evaluate.
    :param filter: List of folders to ignore.
    :return: List of folders to evaluate.
    """
    from os import listdir
    from os.path import isdir, join
    # Get Folders
    directories_only = [dir for dir in listdir(path) if isdir(join(path,dir)) and dir not in filter]
    return directories_only

def _get_logfile_index(path: str) -> tuple[str]:
    """
    Returns the index of the logfile.
    :param path: Path to the logfile.
    :return: Index of the logfile as a tuple.
    """
    from os.path import sep
    with open(path, "r") as f:
        lines_with_index = [l for l in f.readlines() if "--lfc" in l]
        if len(lines_with_index) == 0:
            # No logfile index found, return folders "_index" instead
            path_split = path.split(sep)
            index = path_split[:-2].split("_")[-1]
            return index
        logfile_index_str = lines_with_index[0].split("--lfc")[1].split()[0]
        logfile_index_str = logfile_index_str.split(",")
        index = tuple([s.strip() for s in logfile_index_str])
        if len(index) == 1:
            return index[0], None
        return index
    
def _guess_delimiter(path: str) -> str:
    """
    Guesses the delimiter of a data line.
    :param path: Path to any file.
    :return: Delimiter of the data line.
    """
    with open(path, "r") as src:
        # Read second line only
        data = src.readlines(2)[-1]
        delimiters = [" ", "\t", ",", ";"]
        for d in delimiters:
            if len(data.split(d)) > 1:
                return d
    return " "

def _guess_file_lines(path: str) -> int:
    """
    Guesses the length of a file in lines
    :param path: Path to any file.
    :return: Length of the file in lines.
    """
    with open(path, "r") as src:
        # Read second line only
        data = src.readlines()
        return len(data)
    return 0

def _get_data_header(path: str, delimiter: str =" ", output_delimiter: str | None = None) -> str:
    """
    Returns the header of a data line.
    :param path: Path to any file.
    :param delimiter: Delimiter of the data line.
    :param output_delimiter: Delimiter of the output data line.
    :return: Header of the data line.
    """
    if output_delimiter is None:
        output_delimiter = delimiter
    with open(path, "r") as src:
        # Read first line only
        data = src.readline()
    return output_delimiter.join(data.split(delimiter))
        

def _generate_data_lines(index: tuple[str], data: list[str], delimiter: str = " ") -> list[str]:
    """
    Generates a data line for the logfile.
    :param index: Index of the data line.
    :param data: Data.
    :param delimiter: Delimiter of the data line.
    :return: New Data line that followes 'index1 [index2] data...'.
    """
    # List Data
    if not isinstance(data, list):
        data = [data]
    ret = []
    for d in data:
        # Head Index
        current = f"{index[0]}{delimiter}{d.rstrip()}" if index[1] == None else f"{index[0]}{delimiter}{index[1]}{delimiter}{d.rstrip()}"
        ret.append(current)
    return ret

def _final_point_filter(data: list[str], filter, delimiter: str = " ") -> list[str]:
    """
    Returns the maximum value of the given data. Executes the filter columnwise, or for the i'th column if i is not None
    :param data: Data to filter.
    :param filter: Filter lambda to apply. Must only return a single value.
    :return: Maximum value of the given data.
    """
    # Split lines into columns
    filter_data = zip(*[line.split(delimiter) for line in data])
    # Apply Filter
    filter_data = [filter(column) for column in filter_data]
    # Make sure all values are lists
    #print(filter_data)
    filter_data = [column if isinstance(column, list) or isinstance(column, tuple) else [column] for column in filter_data]
    #print(filter_data)
    # Transpose data back to lines and return
    return [delimiter.join(row) for row in zip(*filter_data)]

def _matrix_filter(data: list[str], filter, replacement = None, delimiter: str = "") -> list[str]:
    """
    Removes all lines from the data that do not match the filter and replaces the values with the replacement value or approximates a suitable value instead.
    :param data: Data to filter.
    :param filter: Filter lambda to apply. Must return a boolean value.
    :param replacement: Replacement lambda. Must return a single value.
    :return: Filtered data.
    """
    filter_data = list(zip(*[line.split(delimiter) for line in data]))
    for i, column in enumerate(filter_data):
        for j, value in enumerate(column):
            if not filter(value):
                continue
            if replacement == None:
                # Approximate a suitable value
                approximated_value = filter_data[i][j-1] if j > 0 else filter_data[i][j+1]
                k = 2
                while filter(approximated_value) == True:
                    approximated_value = filter_data[i][j-k] if j-k >= 0 else filter_data[i][j+k]
                    k += 1
                    if j+k > len(filter_data[i]):
                        filter_data[i] = list(filter_data[i])
                        filter_data[i][j] = "0"
                        break
            else:
                # Replace with replacement value
                filter_data[i] = list(filter_data[i])
                filter_data[i][j] = replacement(filter_data[i][j])
    return [delimiter.join(row) for row in zip(*filter_data)]

def _reshape_data_set(data):
    from numpy import reshape
    x,y = data[0], data[1]
    n = len(set(x))
    m = int(len(x)/n)
    try:
        p = reshape(y,(m,n))
    except Exception as e:
        m = len(set(y))
        n = int(len(x)/m)
    # Reshape data elements
    data = [reshape(d,(m,n)) for d in data]
    return data

def _interpolate_data(data: list[str], index: int = 0, points: int = 100, delimiter: str = " ") -> list[str]:
    """
    Interpolates the given data to the given number of points.
    :param data: Data to interpolate.
    :param twoD: If the data is two dimensional.
    :param points: Number of points to interpolate to.
    :return: Interpolated data.
    """
    from numpy import linspace
    from scipy.interpolate import interp1d
    # Split lines into columns and convert to float
    data = list(zip(*[[float(el) for el in line.split(delimiter)] for line in data]))
    # Interpolate a numpy matrix from N X M points to poinst X points:
    new_x = linspace(data[index][0], data[index][-1], points)

    data = [new_x] + [interp1d(data[index], column, kind="linear")(new_x) for column in data[1:]] 
    # Transpose data back to lines, convert to string and return
    data = [delimiter.join([str(el) for el in column]) for column in zip(*data)]
    return data

def _clean_data(data: list[str], file_delimiter: str = " ", output_delimiter: str = " ") -> list[str]:
    for i, line in enumerate(data):
        while f"{file_delimiter}{file_delimiter}" in line:
            line = line.replace(f"{file_delimiter}{file_delimiter}", file_delimiter)
        data[i] = output_delimiter.join(line.rstrip().split(file_delimiter))
    return data

def _guess_extraction_mode(path: str) -> tuple[str]:
    """
    Guesses the extraction mode of the given file.
    :param str: Path to the file.
    :return: Extraction mode.
    """
    logfile_index = _get_logfile_index(path)
    if logfile_index[1] is None:
        return "set_of_calculations_to_matrix", "set_of_calculations_to_endpoint"
    return "set_of_calculations_to_endpoint_matrix", 

def _input_to_tuple(input: str, delimiter: str = ":") -> tuple[str]:
    return tuple(input.split(delimiter))


if __name__ == "__main__":
    print("This file is part of the QDLC evaluation framework and should not be executed on its own.")