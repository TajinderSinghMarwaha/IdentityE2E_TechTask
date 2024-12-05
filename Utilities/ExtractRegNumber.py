import os
import re
from configuration.config import TestData

# Folder path containing files
folder_path = os.path.join(os.getcwd(), "resources", "Test_Input_Files")

# Regular expression to match registration numbers
reg_pattern = r"\b[A-Z]{2}[0-9]{2}\s?[A-Z]{3}\b"

# Function to extract registration numbers from a file
def extract_reg_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return re.findall(reg_pattern, content)



def read_file(file_path, filename):
    all_reg_numbers = []
    # Ensure it's a file (not a directory)
    if os.path.isfile(file_path):
        try:
            reg_numbers = extract_reg_numbers(file_path)
            all_reg_numbers.extend(reg_numbers)
            print(f"File: {filename}")
            print(f"Extracted Registration Numbers: {reg_numbers}\n")
        except Exception as e:
            print(f"Error reading file {filename}: {e}")

    # Print all collected registration numbers
    print("All Extracted Registration Numbers:", all_reg_numbers)
    return all_reg_numbers