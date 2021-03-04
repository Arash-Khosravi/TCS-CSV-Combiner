"""
TO watch the folder for 'Adding new CSV files' to it, the module of WATCHDOG has been used which waits for events and
changes in SystemFiles.
please check https://pypi.org/project/watchdog/ for more information
"""

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from csv_folder_wrapper import directories
from data_frame_maker import data_frame_maker


class Watcher:
    """
    The watcher Class is for ease of use in the main.py
    """
    DIRECTORY_TO_WATCH = directories()  # Path of the folder to be watched

    def __init__(self):
        self.observer = Observer()

    def run(self):
        """
        This function will run the watcher and makes a Handler object,
        """
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()  # Starting the watch
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    """
    This class will make a different handler type, for each time a new file added to the folder,
    Take any action for every event.event_type, you can add events, as many as you need for different circumstances.
    Please check WatchDog documentation for more help.
    """

    @staticmethod
    def on_any_event(event):
        """
        This function will wait for any changes (events) in the folder and will be execute any script or action if
        that particular event happened.
        :param event: event object of Watchdog
        :return: Nothing, will execute any script or action under events
        """
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            """
            Will trigger the data_frame_maker func if now file added to the folder
            """
            # Taken any action here when a file added to the folder (created).
            data_frame_maker()
            print(f"Received new CSV file at:\n {event.src_path}")
            print(type(event.src_path))

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print(f"Received modified event - {event.src_path}")
