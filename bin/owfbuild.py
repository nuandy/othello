import os
import sys
import getopt
import xml.dom.minidom

"""owfbuild.py by Andy Nu nuandy@gmail.com
This script accepts one option.
To build a specific app in the apps directory, try: python owfbuild.py --app=foo where foo is the directory name of your app.
"""

xml_version = '1.0'
encoding = 'UTF-8'
app_arg = ''

options, extraparams = getopt.getopt(sys.argv[1:], '', ['app='])

path = os.path.realpath('.')
base = os.path.basename(path)

def listapps():
  if base == 'othello':
    os.chdir(os.path.abspath(os.curdir)+'/apps')
    apps = [name for name in os.listdir('.') if os.path.isdir(name)]
    os.chdir(os.path.pardir)
  else:
    sys.exit("Oops! This script must be run within the root/top level othello directory!")
  return apps

apps_collection = listapps()

def touch(fname, times = None):
  with file(fname, 'a'):
    os.utime(fname, times)

def servletmapping():
  if base == 'othello':
    for opt, arg in options:
      if opt in ('--app'):
        app_arg = arg
        app_exists = 'false'
        for name in apps_collection:
          if app_arg == name:
            app_exists = 'true'
            break
          else:
            app_exists = 'false'
        if app_exists == 'true':
          os.chdir(os.path.abspath(os.curdir)+'/apps/'+app_arg)
          os.chdir('WEB-INF')
          xmldoc = xml.dom.minidom.parse('web.xml')
          for node in xmldoc.getElementsByTagName('web-app'):
            for subnode in xmldoc.getElementsByTagName('servlet-mapping'):
              node.removeChild(subnode)
          os.chdir(os.path.pardir)
          os.chdir('conf')
          xmldocroutes = xml.dom.minidom.parse('routes.xml')
          for route in xmldocroutes.getElementsByTagName('routes'):
            for routeurl in xmldocroutes.getElementsByTagName('url'):
              print 'Associating '+ routeurl.firstChild.nodeValue + ' found in routes.xml with WEB-INF/web.xml'
              servletmapping = xmldoc.createElement('servlet-mapping')
              servletname = xmldoc.createElement('servlet-name')
              baseservlet = xmldoc.createTextNode('BaseServlet')
              urlpattern = xmldoc.createElement('url-pattern')
              url = xmldoc.createTextNode(routeurl.firstChild.nodeValue)
              servletname.appendChild(baseservlet)
              urlpattern.appendChild(url)
              servletmapping.appendChild(servletname)
              servletmapping.appendChild(urlpattern)
              for node in xmldoc.getElementsByTagName('web-app'):
                node.appendChild(servletmapping)
          os.chdir(os.path.pardir)
          os.chdir('WEB-INF')
          f = open('web.xml', 'w')
          f.write(xmldoc.toxml())
          f.close()
          os.chdir(os.path.pardir)
          os.chdir(os.path.pardir)
          os.chdir(os.path.pardir)
  else:
    sys.exit("Oops! This script must be run within the root/top level othello directory!")

servletmapping()

#if specific app name argument is passed in...
for opt, arg in options:
  if opt in ('--app'):
    app_arg = arg
    app_exists = 'false'
    for name in apps_collection:
      if app_arg == name:
        app_exists = 'true'
        break
      else:
        app_exists = 'false'
    if app_exists == 'true':
      xmlstring =  '<?xml version="' + xml_version + '" encoding="' + encoding  + '" ?>\n'
      xmlstring += '<project name="othello" basedir="." default="main">\n'
      xmlstring += '<property name="build.compiler" value="org.eclipse.jdt.core.JDTCompilerAdapter"/>\n'
      xmlstring += '<property name="lib.dir"     value="lib"/>\n'
      xmlstring += '<property name="apps.dir"    value="apps"/>\n'
      xmlstring += '<property name="build.dir"   value="build"/>\n'
      xmlstring += '<property name="classes.dir" value="${build.dir}/classes"/>\n'
      xmlstring += '<property name="jar.dir"     value="release"/>\n'
      xmlstring += '<property name="war.dir"     value="release"/>\n'
      xmlstring += '<property name="'+app_arg+'.dir"    value="apps/'+app_arg+'"/>\n'
      xmlstring += '<property name="'+app_arg+'.name"   value="'+app_arg+'"/>\n'
      xmlstring += '<path id="classpath">\n'
      xmlstring += '<fileset dir="${lib.dir}" includes="**/*.jar"/>\n'
      xmlstring += '</path>\n'
      xmlstring += '<target name="clean">\n'
      xmlstring += '<delete dir="${build.dir}"/>\n'
      xmlstring += '</target>\n'
      xmlstring += '<target name="compile">\n'
      xmlstring += '<mkdir dir="${classes.dir}"/>\n'
      xmlstring += '<copy todir="${build.dir}/static">\n'
      xmlstring += '<fileset dir="${'+app_arg+'.dir}" excludes="**/*.java"/>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<javac source="1.6" target="1.6" srcdir="${'+app_arg+'.dir}" destdir="${classes.dir}" classpathref="classpath" includeantruntime="false" compiler="org.eclipse.jdt.core.JDTCompilerAdapter"/>\n'
      xmlstring += '</target>\n'
      xmlstring += '<target name="jar" depends="compile">\n'
      xmlstring += '<jar destfile="${jar.dir}/${'+app_arg+'.name}/${'+app_arg+'.name}.jar" basedir="${classes.dir}"/>\n'
      xmlstring += '</target>\n'
      xmlstring += '<target name="war" depends="jar">\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app_arg+'.name}/WEB-INF/lib" preservelastmodified="true">\n'
      xmlstring += '<fileset dir="${lib.dir}/${ant.project.name}">\n'
      xmlstring += '<include name="**/*.jar" />\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app_arg+'.name}" preservelastmodified="true">\n'
      xmlstring += '<fileset dir="${build.dir}/static">\n'
      xmlstring += '<exclude name="**/*.java"/>\n'
      xmlstring += '<include name="**/**"/>\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app_arg+'.name}/WEB-INF/lib" preservelastmodified="true" flatten="true">\n'
      xmlstring += '<fileset dir="${lib.dir}">\n'
      xmlstring += '<include name="**/*.jar" />\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app_arg+'.name}/WEB-INF/lib" preservelastmodified="true" flatten="true">\n'
      xmlstring += '<fileset dir="${jar.dir}/${'+app_arg+'.name}">\n'
      xmlstring += '<include name="**/*.jar" />\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app_arg+'.name}/WEB-INF/classes" preservelastmodified="true" flatten="true">\n'
      xmlstring += '<fileset dir="${apps.dir}">\n'
      xmlstring += '<include name="log4j.properties" />\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<jar destfile="${war.dir}/${'+app_arg+'.name}.war" basedir="${build.dir}/tmp/${'+app_arg+'.name}" />\n'
      xmlstring += '<delete dir="${jar.dir}/${'+app_arg+'.name}"/>\n'
      xmlstring += '</target>\n'
      xmlstring += '<target name="main" depends="clean,war">\n'
      xmlstring += '<echo>Congrats, you just built '+app_arg+'!</echo>\n'
      xmlstring += '</target>\n'
      xmlstring += '</project>\n'
      #write to build.xml and run ant...
      f = open('build.xml', 'w')
      f.write(xmlstring)
      f.close()
      if os.path.isfile('build.xml'):
        os.system(path + '/bin/ant/bin/ant -lib ' + path + '/lib/compiler/ecj.jar')
        os.chdir('contexts')
        touch('context.xml')
        os.chdir(os.path.pardir)
    else:
      print 'Oops! No app by that name exists in the apps directory.'

if app_arg == '':
  print 'This script accepts one option.\n'
  print 'To build a specific app in the apps directory, try: python owfbuild.py --app=foo\n'
  print 'where foo is the directory name of your app.\n'
