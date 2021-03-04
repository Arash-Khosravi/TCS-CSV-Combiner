from filename_cleaner import not_alphabetic
from csv_folder_wrapper import root_csv_finder
import pandas as pd
import numpy as np
import socket
import os


# Global dictionary of data
li = {'Source IP': [], 'Environment': []}


def data_frame_maker():
    """
    This function will be read all files in the CSV container folder which comes from 'csv_finder' func,
    after checking the filename by using 'not-alphabetical' function,
    after preparation will trigger the data_completer func by sending the dictionary to it.
    :return: None <-- will trigger the data_completer func
    """
    for filename in root_csv_finder():  # Reading all files
        if filename.split(sep='/')[-1] == 'Combined.csv':  # Skips the combined.csv file
            continue
        else:
            df = pd.read_csv(filename, header=0)  # Using Pandas Library to make a DataFrame
            correct_file_name = not_alphabetic(filename)  # Checking the file name
            ips = df['Source IP'].tolist()
            for x in ips:
                li['Source IP'].append(x)
                li['Environment'].append(correct_file_name)
    data_completer(li)


def add_new_data(file):
    """
    This function will be triggered if a new CSV adds to the folder,
    after preparation executes 'data_completer' function
    :param file: name of the new added file
    :return: None <-- will trigger the data_completer func
    """
    path = os.getcwd()
    complete_file_with_path = path + '/' + file[0]
    df = pd.read_csv(complete_file_with_path, header=0)
    correct_file_name = not_alphabetic(complete_file_with_path)
    ips = df['Source IP'].tolist()
    for x in ips:
        li['Source IP'].append(x)
        li['Environment'].append(correct_file_name)
    data_completer(li)


def data_completer(li_dict=None):
    """
    To transform the dictionary to the Pandas Dataframe, cleans the duplicated info, sorts the
    DataFrame by Source IP, and make 'Combined.csv' file.
    To sort 'Source IP' column uses Numpy and Socket libraries, which sorts string as Integer
    :param li_dict: Any dictionary <-- the li dictionary which made by 'data_frame_maker'
    :return: None <-- The Combined.csv file will be Created
    """
    if li_dict is None:
        li_dict = li
    data = pd.DataFrame.from_dict(li_dict, orient='columns')
    data.drop_duplicates(inplace=True)
    # Using Numpy and Socket libraries to sort 'Source IP' column, which sorts string as  Integer
    data = data.iloc[np.argsort(list(map(socket.inet_aton, data['Source IP'])))]
    data.to_csv('Combined.csv', index=False)


