"""
Function to clean the file name as needed for dataframe and Environments
The assumption is we need first 2 syllabus each file name, will be modified in future sprints if the file name types
going to be change
"""


def not_alphabetic(file):
    """
    This function will check file name and make a necessary changes to delete all NONE ALPHABETICAL characters
    from end of the file, one by one.
    To delete the other type of extensions, add them to the extensions list
    :param file: should be the complete path of the file
    :return: The clean file name, to be used in dataframe
    """
    file = file.replace('csv', '')  # Deleting the file extension
    if '/' in file:
        file = file.split(sep='/')[-1]  # Splitting the file by '/' if it contains it
    else:
        pass

    the_file_name = file
    if not the_file_name[-1].isalpha():  # Checking if the last part of split is Alphabetical
        while not the_file_name[-1].isalpha():
            the_file_name = the_file_name.rstrip()  # Deleting the whitespace from right of the file name
            the_file_name = the_file_name[:-1]
            the_file_name = the_file_name.rstrip()

    return the_file_name
