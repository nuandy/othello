import os
import sys
import subprocess
import datetime
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = os.path.realpath('.')
base = os.path.basename(path)

def get_now():
  return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def build_app():
  print >> sys.stderr, "Building app at %s" % get_now()
  subprocess.call('python bin/owfbuild.py --app='+sys.argv[2], shell=True)

class ChangeHandler(FileSystemEventHandler):
  def on_any_event(self, event):
    build_app()

def main():
  event_handler = ChangeHandler()
  observer = Observer()
  observer.schedule(event_handler, path=sys.argv[1], recursive=True)
  observer.start()
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

if __name__ == '__main__':
  main()
