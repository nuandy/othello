import sys
import os
import subprocess

path = os.path.realpath('.')
base = os.path.basename(path)

if base == 'othello':
  subprocess.call('java -DSTART=' + path + '/server/start.config -jar ' + path + '/server/start.jar ' + path + '/server/config/jetty.xml', shell=True)
else:
  sys.exit('Oops! This script must be run at the root/top level othello directory!')
