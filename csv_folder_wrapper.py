import glob
import os


def directories(csv_folder_name='Engineering Test Files'):
    """
    This function will check if the folder which contains csv files exist or not,
     and if not, will create it (In this case by the name of 'Engineering Test Files' and
     returns the complete path of csv folder to be used in other functions
    :param csv_folder_name: defaulted as 'Engineering Test Files'
    :return: complete path of csv folder
    """

    path = os.getcwd()  # Getting the path of working directory --> os module

    try:  # Checking if folder exist or not
        if os.path.isdir(csv_folder_name):
            return path + '/' + csv_folder_name
    except FileExistsError:
        print(f'The folder which contains CSV files does not exist,'
              f' we will make it by the name of {csv_folder_name}, please add csv files into it')
        pass
    else:  # Creating the folder in the working directory
        os.mkdir(csv_folder_name)
        return path + csv_folder_name


def root_csv_finder(path=directories()):
    """
    This function uses glob module to make a list of .csv files which are in CSV files directory
    :param path: the full path of csv files directory
    :return: the list of all csv files in the that folder
    """

    os.chdir(path)  # Switching working path to root path
    all_files = glob.glob(os.path.join(path, "*.csv"))
    return all_files


