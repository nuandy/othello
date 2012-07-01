import sys
import os
import subprocess
import getopt
import re

app_key = ''

options, extraparams = getopt.getopt(sys.argv[1:], '', ['app='])

path = os.path.realpath('.')
base = os.path.basename(path)

def listapps():
  if base == 'othello':
    os.chdir(os.path.abspath(os.curdir)+'/apps')
    apps = [name for name in os.listdir('.') if os.path.isdir(name)]
    os.chdir(os.path.pardir)
  elif base == 'bin':
    os.chdir(os.path.pardir+'/apps')
    apps = [name for name in os.listdir('.') if os.path.isdir(name)]
    os.chdir(os.path.pardir)
  else:
    sys.exit("Oops! This script must be run within the root/top level othello directory or othello/bin!")
  return apps

def process_exists(process_name):
  ps = subprocess.Popen("ps ax -o pid= -o args= ", shell=True, stdout=subprocess.PIPE)
  ps_pid = ps.pid
  output = ps.stdout.read()
  ps.stdout.close()
  ps.wait()

  for line in output.split("\n"):
    results = re.findall("(\d+) (.*)", line)
    if results:
      pid = int(results[0][0])
      if process_name in results[0][1] and pid != os.getpid() and pid != ps_pid:
        return pid
  return False

apps_collection = listapps()

if base == 'othello':
  for opt, arg in options:
    if opt in ('--app'):
      app_key = arg
      app_exists = 'false'
      for name in apps_collection:
        if app_key == name:
          app_exists = 'true'
          break
        else:
          app_exists = 'false'
      if app_exists == 'true':
        start_command = 'java -DSTART=' + path + '/server/start.config -jar ' + path + '/server/start.jar ' + path + '/server/config/jetty.xml'
        monitor_command = 'python bin/monitor.py ' + path + '/apps/'+app_key+'/app ' + app_key
        start_pid = process_exists(start_command)
        monitor_pid = process_exists(monitor_command)
        if start_pid == False:
          subprocess.Popen(start_command, shell=True)
        else:
          print 'An othello server process is already running!'
          print 'Killing process ' + str(start_pid)
          os.kill(start_pid, 9)
          print 'Starting a new othello server process...'
          subprocess.Popen(start_command, shell=True)
        if monitor_pid == False:
          subprocess.Popen(monitor_command, shell=True)
        else:
          print 'An othello monitoring process is already running!'
          print 'Killing process ' + str(monitor_pid)
          os.kill(monitor_pid, 9)
          print 'Starting a new othello monitoring process...'
          subprocess.Popen(monitor_command, shell=True)
      else:
        sys.exit('Oops! No app by that name exists in the apps directory.')
else:
  sys.exit('Oops! This script must be run at the root/top level othello directory!')

if app_key == '':
  print 'This script accepts one option.\n'
  print 'To start a specific app in the apps directory, try: python owfstart.py --app=foo\n'
  print 'where foo is the directory name of your app.\n'
