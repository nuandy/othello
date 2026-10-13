import os

"""owfcontext.py
Shared by owfbuild.py and owfstart.py. Jetty deploys whichever war contexts/context.xml names,
so building or starting an app points it at release/<app>.war. Rewriting the file also tells a
running Jetty to redeploy.
"""

def war_path(path, app_key):
  return path + '/release/' + app_key + '.war'

def write_context(path, app_key):
  xmlstring =  '<?xml version = "1.0" encoding = "utf-8"?>\n'
  xmlstring += '<Configure class="org.mortbay.jetty.webapp.WebAppContext">\n'
  xmlstring += '  <Set name="contextPath">/</Set>\n'
  xmlstring += '  <Set name="war"><SystemProperty name="jetty.home" default="."/>/release/' + app_key + '.war</Set>\n'
  xmlstring += '</Configure>\n'
  f = open(os.path.join(path, 'contexts', 'context.xml'), 'w')
  f.write(xmlstring)
  f.close()
