import os

def compare_files_line_by_line(file1_path, file2_path, search_variable):
    """
    Search for a specific variable in two files, extract the corresponding lines, and compare them.

    Parameters:
    file1_path (str): Path to the first/actual text file.
    file2_path (str): Path to the second/expected text file.
    search_variable (str): The string to search for in each line of the files.

    Returns:
    tuple: A tuple containing the lines from both files and whether they match.
    """
    try:
        # Read lines from both files
        print("file1_path:", file1_path)
        print("file2_path:", file2_path)

        print("file1_path repr:", repr(file1_path))
        print("file2_path repr:", repr(file2_path))
        with open(file1_path, 'r') as file:
            print(file.read())
        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()


        # Normalize lines: Remove extra spaces and newlines
        normalized_lines1 = [line.replace(" ", "").strip() for line in lines1]
        normalized_lines2 = [line.replace(" ", "").strip() for line in lines2]
        # Find the lines containing the search variable
        line1 = next((line.strip() for line in normalized_lines1 if search_variable in line), None)
        line2 = next((line.strip() for line in normalized_lines2 if search_variable in line), None)

        # Compare the lines
        if line1 is None or line2 is None:
            return (line1, line2, False, "Search variable not found in one or both files")

        return (line1, line2, line1 == line2, None)

    except FileNotFoundError as e:
        return [f"Error: {e}"]

def compare_fetch_reg_compare(version, search_variable):
    """
    fetch the reg numbers from input file and compare the actual and expected.

    Parameters:
    version: version of file to be compared.
    search_variable (str): The string to search for in each line of the files.

    Returns:
    line1, line2, is_match, error_message = results
    """

    expected_folder_path = os.path.join(os.getcwd(), "resources", "Expected_Output_Files")
    actual_folder_path = os.path.join(os.getcwd(), "resources", "Actual_Output_Files")

    file_expected = version.replace("car_input", "car_output")
    file_actual = version.replace("car_input", "actual_output")


    file_expected_path = os.path.abspath(expected_folder_path + "/" + file_expected)
    file_actual_path = os.path.abspath(actual_folder_path + "/" + file_actual)
    search_variable = search_variable


    results = compare_files_line_by_line(file_actual_path, file_expected_path,  search_variable)

    print("results:", results)

    line1, line2, is_match, error_message = results

    if error_message:
        print(error_message)
        return "Mismatch"
    else:
        if is_match:
            print(f"Match found:\nFile1: {line1}\nFile2: {line2}")
            return "Match"
        else:
            print(f"Mismatch:\nFile1: {line1}\nFile2: {line2}")
            return "Mismatch"