"""
Please execute main.py to start the app first,
Due to type of requirements of this project, app would not have any possibility to stop or quit by user (except Ctrl+C)
Move the files from ""Engineering Test Files" folder and add them
You can add drag-drop csv file to the "Engineering Test Files".
This mini app will work continuously to check the changes in CSV files folder and add the data as requested to the
'Combined.csv' file.
If the "Engineering Test Files" folder does not exist, the app will create it for you(please add the csv files to it).
If the content of csv files changes, you can add them again to the folder and the app will add the new data to the
"Combined.csv" file.
You can add several csv file to the "Engineering Test Files" simultaneously.
The app will only delete the 100% duplicated data.
The 'Combined.csv' file will be appear several seconds after the first file of data being added.
"""

from event_handler import Watcher


if __name__ == '__main__':
    w = Watcher()
    w.run()