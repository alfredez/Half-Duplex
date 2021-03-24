# import os, time
# path_to_watch = "./correct"
# before = dict([(f, None) for f in os.listdir(path_to_watch)])
# while 1:
#     time.sleep(10)
#     after = dict ([(f, None) for f in os.listdir(path_to_watch)])
#     added = [f for f in after if not f in before]
#     removed = [f for f in before if not f in after]
#     if added: print("Added: ", ", ".join (added))
#     if removed: print("Removed: ", ", ".join (removed))
#     before = after
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "./correct"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
#and '~' not in event.src_path
        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print ("Received modified event - %s." % event.src_path)

        elif event.event_type == 'deleted':
            # Taken any action here when a file is modified.
            print("Received deleted event - %s." % event.src_path)

        elif event.event_type == 'closed':
            # Taken any action here when a file is modified.
            print("Received closed event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()