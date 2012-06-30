import sys
import os
import subprocess
import getopt

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
        subprocess.Popen('java -DSTART=' + path + '/server/start.config -jar ' + path + '/server/start.jar ' + path + '/server/config/jetty.xml', shell=True)
        subprocess.Popen('python bin/monitor.py ' + path + '/apps/'+app_key+'/app ' + app_key, shell=True)
        print path
      else:
        sys.exit('Oops! No app by that name exists in the apps directory.')
else:
  sys.exit('Oops! This script must be run at the root/top level othello directory!')

if app_key == '':
  print 'This script accepts one option.\n'
  print 'To start a specific app in the apps directory, try: python owfstart.py --app=foo\n'
  print 'where foo is the directory name of your app.\n'
