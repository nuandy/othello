import os
import sys
import subprocess
import datetime
import time
import threading
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
  def __init__(self):
    FileSystemEventHandler.__init__(self)
    self.lock = threading.Lock()
    self.last_event = None

  def on_any_event(self, event):
    self.lock.acquire()
    self.last_event = time.time()
    self.lock.release()

  def take_pending(self, quiet_secs):
    #true once events have stopped arriving for quiet_secs, so a burst of saves builds once
    self.lock.acquire()
    try:
      if self.last_event is not None and time.time() - self.last_event >= quiet_secs:
        self.last_event = None
        return True
      return False
    finally:
      self.lock.release()

def main():
  event_handler = ChangeHandler()
  observer = Observer()
  observer.schedule(event_handler, path=sys.argv[1], recursive=True)
  observer.start()
  try:
    while True:
      time.sleep(1)
      if event_handler.take_pending(1):
        build_app()
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

if __name__ == '__main__':
  main()
