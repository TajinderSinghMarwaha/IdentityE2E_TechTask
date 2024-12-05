import os

def create_or_replace_file(file_path, lines):
    """
    Deletes the file if it exists and creates a new one with the given lines.

    Args:
        file_path (str): Path of the file to create or replace.
        lines (list): List of strings to write to the file.

    Returns:
        None
    """
    # Example usage
    folder_path = os.path.join(os.getcwd(), "resources", "Actual_Output_Files")
    print("folder location for actual output:", folder_path)
    # Check if the file exists and delete it
    file_path_new = file_path.replace("car_input", "actual_output")
    file_path = os.path.join(folder_path, file_path_new)
    print("file_path for actual output:", file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted existing file: {file_path}")

    # Create a new file and write the provided lines
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + "\n")

    print(f"New file created and text written to: {file_path}")

