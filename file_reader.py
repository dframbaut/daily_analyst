import os
import pandas as pd
from data_contract import compare_columns

# Function to read CSV files
def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path, sep='|')
        if df.empty and df.columns.size == 0:
            return 'empty'
        return df
    except pd.errors.EmptyDataError:
        return 'empty'
    except Exception as e:
        print(f'Could not process file {file_path}: {e}')
        return None

# Function to list folders
def list_folders(parent_path):
    folders = sorted([name for name in os.listdir(parent_path) if os.path.isdir(os.path.join(parent_path, name))], reverse=True)
    if not folders:
        print("No folders found in the specified path.")
        return []
    print("\nFound folders:")
    for i, folder in enumerate(folders, 1):
        print(f"{i}. {folder}")
    return folders

# Function to select a folder
def select_folder(parent_path, selection, folders):
    # If the selection is a number
    if selection.isdigit():
        index = int(selection) - 1
        if 0 <= index < len(folders):
            return os.path.join(parent_path, folders[index])
        else:
            print("Invalid selection.")
            exit()
    # If the selection is a folder name
    elif selection in folders:
        return os.path.join(parent_path, selection)
    else:
        print("Invalid selection.")
        exit()

# Function to retrieve file records in order (with two columns)
def get_records_data(folder_path, prefixes, suffix_order):
    records_data = []  # Matrix that will contain two columns: [number of records, file name]

    # Get all CSV files
    csv_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.csv')])

    # Sort files by prefixes and suffixes
    for prefix in prefixes:
        for suffix in suffix_order:
            for file in csv_files:
                if file.startswith(prefix) and suffix in file:
                    full_path = os.path.join(folder_path, file)
                    df = read_csv_file(full_path)
                    
                    if df is not None:
                        # Determine the number of records or if the file is empty
                        if isinstance(df, str) and df == 'empty':
                            records_data.append(['empty file', file])  # Empty file without header
                        else:
                            num_records = len(df)  # Number of records
                            records_data.append([num_records, file])
                    else:
                        records_data.append(['error reading file', file])  # If there was an error reading the file
    
    return records_data

# Function to retrieve files with column mismatches, returning a matrix with three columns
def get_mismatch_files(folder_path, expected_columns, prefixes, suffix_order):
    mismatch_files = []  # Matrix that will contain three columns: [file name, expected columns, found columns]

    # Get all CSV files
    csv_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.csv')])

    for prefix in prefixes:
        for suffix in suffix_order:
            for file in csv_files:
                if file.startswith(prefix) and suffix in file:
                    full_path = os.path.join(folder_path, file)
                    df = read_csv_file(full_path)
                    
                    # Only process DataFrames (valid files with headers)
                    if df is not None and isinstance(df, pd.DataFrame):
                        actual_columns = df.columns.tolist()  # Found columns
                        table_name = file.split('-')[1]  # Identify the table by file name
                        
                        # Compare columns if expected columns exist
                        if table_name in expected_columns:
                            expected_cols = expected_columns[table_name]  # Expected columns
                            columns_match = compare_columns(file, expected_cols, actual_columns)
                            
                            # If columns don't match, add to mismatch_files matrix
                            if not columns_match:
                                mismatch_files.append([file, expected_cols, actual_columns])

    return mismatch_files

# Function to retrieve valid files (with at least one record)
def get_valid_files(folder_path, prefixes, suffix_order):
    valid_files = []

    # Get all CSV files
    csv_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.csv')])

    for prefix in prefixes:
        for suffix in suffix_order:
            for file in csv_files:
                if file.startswith(prefix) and suffix in file:
                    full_path = os.path.join(folder_path, file)
                    df = read_csv_file(full_path)
                    if isinstance(df, pd.DataFrame) and len(df) > 0:
                        valid_files.append((file, df))  # Store file and DataFrame
    
    return valid_files

# Function to check for missing expected files using prefixes and suffixes
def check_expected_files(folder_path, expected_files):
    # Get all existing files in the folder
    existing_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Create a set of expected files by combining prefixes and suffixes
    expected_set = set(expected_files)
    
    # Check if any expected files are missing
    missing_files = [expected_file for expected_file in expected_set if not any(expected_file in file for file in existing_files)]
    
    return missing_files