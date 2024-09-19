# list files in session_reports directory

import os
import pandas as pd

def list_files():
    file_list = []
    # list files in session_reports directory
    for root, dirs, files in os.walk("session_reports"):
        for file in files:
            file_list.append(file)
            print(file)
    return file_list
            
files = list_files()
    
print(files)


# for each file read in first sheet and append to a list, create a column called date with first 5 charcters of the file name
# and save to a new file called all_sessions.csv


def list_files():
    file_list = []
    # list files in session_reports directory
    for root, dirs, files in os.walk("session_reports"):
        for file in files:
            file_list.append(file)
            print(file)
    return file_list
            
files = list_files()
    
print(files)

def read_files(files):
    all_sessions = []
    for file in files:
        file_path = os.path.join("session_reports", file)
        date = file[:6]
        
        # Check the file extension and read accordingly
        if file.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file.endswith('.xlsx'):
            df = pd.read_excel(file_path, sheet_name=0)
        else:
            continue  # Skip files that are neither CSV nor Excel
        
        df['date'] = date
        all_sessions.append(df)
        print("Appended", file)
    
    # Concatenate all DataFrames in the list
    all_sessions_df = pd.concat(all_sessions, ignore_index=True)
    return all_sessions_df

all_sessions = read_files(files)

all_sessions.to_csv('all_sessions.csv', index=False)