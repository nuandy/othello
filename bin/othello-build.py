import os
import sys
import getopt

"""othello.py by Andy Nu nuandy@gmail.com
This script accepts two options.
1) To build a specific app in the apps directory, try: python othello.py --app=foo
   where foo is the directory name of your app.
2) To build all the apps in the apps directory, try: python othello.py --buildall
"""

xml_version = '1.0'
encoding = 'utf-8'
app_arg = ''
buildall = False

options, extraparams = getopt.getopt(sys.argv[1:], '', ['app=',
                                                        'buildall',
                                                        ])

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
      xmlstring += '<property name="othello.dir" value="framework"/>\n'
      xmlstring += '<property name="src.dir"     value="apps"/>\n'
      xmlstring += '<property name="lib.dir"     value="lib"/>\n'
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
      xmlstring += '<target name="compile-framework">\n'
      xmlstring += '<mkdir dir="${classes.dir}/${ant.project.name}"/>\n'
      xmlstring += '<copy todir="${classes.dir}/${ant.project.name}">\n'
      xmlstring += '<fileset dir="${othello.dir}" excludes="**/*.java"/>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<javac srcdir="${othello.dir}" destdir="${classes.dir}/${ant.project.name}" classpathref="classpath" includeantruntime="false"/>\n'
      xmlstring += '</target>\n'
      xmlstring += '<target name="compile">\n'
      xmlstring += '<mkdir dir="${classes.dir}"/>\n'
      xmlstring += '<copy todir="${classes.dir}">\n'
      xmlstring += '<fileset dir="${src.dir}" excludes="**/*.java"/>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<javac srcdir="${src.dir}" destdir="${classes.dir}" classpathref="classpath" includeantruntime="false"/>\n'
      xmlstring += '</target>\n'
      xmlstring += '<target name="jar-framework" depends="compile-framework">\n'
      xmlstring += '<jar destfile="${lib.dir}/${ant.project.name}/${ant.project.name}.jar" basedir="${classes.dir}/${ant.project.name}"/>\n'
      xmlstring += '</target>\n'
      xmlstring += '<target name="jar" depends="compile">\n'
      xmlstring += '<mkdir dir="${jar.dir}/${'+app_arg+'.name}"/>\n'
      xmlstring += '<jar destfile="${jar.dir}/${'+app_arg+'.name}/${'+app_arg+'.name}.jar" basedir="${classes.dir}"/>\n'
      xmlstring += '</target>\n'
      xmlstring += '<target name="war" depends="jar-framework,jar">\n'
      xmlstring += '<delete dir="${build.dir}/tmp"/>\n'
      xmlstring += '<mkdir dir="${build.dir}/tmp"/>\n'
      xmlstring += '<mkdir dir="${war.dir}"/>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app_arg+'.name}" preservelastmodified="true">\n'
      xmlstring += '<fileset dir="${classes.dir}/${ant.project.name}">\n'
      xmlstring += '<exclude name="**/*.java"/>\n'
      xmlstring += '<include name="**/**"/>\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app_arg+'.name}" preservelastmodified="true">\n'
      xmlstring += '<fileset dir="${classes.dir}/${'+app_arg+'.name}">\n'
      xmlstring += '<exclude name="**/*.java"/>\n'
      xmlstring += '<include name="**/**"/>\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app_arg+'.name}/WEB-INF/lib" preservelastmodified="true" flatten="true">\n'
      xmlstring += '<fileset dir="${lib.dir}">\n'
      xmlstring += '<include name="**/*.jar" />\n'
      xmlstring += '<include name="**/*.zip" />\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app_arg+'.name}/WEB-INF/lib" preservelastmodified="true" flatten="true">\n'
      xmlstring += '<fileset dir="${jar.dir}/${'+app_arg+'.name}">\n'
      xmlstring += '<include name="**/*.jar" />\n'
      xmlstring += '<include name="**/*.zip" />\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<jar destfile="${war.dir}/${'+app_arg+'.name}.war" basedir="${build.dir}/tmp/${'+app_arg+'.name}" />\n'
      xmlstring += '<delete dir="${jar.dir}/${'+app_arg+'.name}"/>\n'
      xmlstring += '<delete dir="${build.dir}/tmp"/>\n'
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
        os.system('ant')
    else:
      print 'Oops! No app by that name exists in the apps directory.'
  elif opt in ('--buildall'):
    buildall = True
    xmlstring =  '<?xml version="' + xml_version + '" encoding="' + encoding  + '" ?>\n'
    xmlstring += '<project name="othello" basedir="." default="main">\n'
    xmlstring += '<property name="othello.dir" value="framework"/>\n'
    xmlstring += '<property name="src.dir"     value="apps"/>\n'
    xmlstring += '<property name="lib.dir"     value="lib"/>\n'
    xmlstring += '<property name="build.dir"   value="build"/>\n'
    xmlstring += '<property name="classes.dir" value="${build.dir}/classes"/>\n'
    xmlstring += '<property name="jar.dir"     value="release"/>\n'
    xmlstring += '<property name="war.dir"     value="release"/>\n'
    for app in apps_collection:
      xmlstring += '<property name="'+app+'.dir"    value="apps/'+app+'"/>\n'
      xmlstring += '<property name="'+app+'.name"   value="'+app+'"/>\n'
    xmlstring += '<path id="classpath">\n'
    xmlstring += '<fileset dir="${lib.dir}" includes="**/*.jar"/>\n'
    xmlstring += '</path>\n'
    xmlstring += '<target name="clean">\n'
    xmlstring += '<delete dir="${build.dir}"/>\n'
    xmlstring += '</target>\n'
    xmlstring += '<target name="compile-framework">\n'
    xmlstring += '<mkdir dir="${classes.dir}/${ant.project.name}"/>\n'
    xmlstring += '<copy todir="${classes.dir}/${ant.project.name}">\n'
    xmlstring += '<fileset dir="${othello.dir}" excludes="**/*.java"/>\n'
    xmlstring += '</copy>\n'
    xmlstring += '<javac srcdir="${othello.dir}" destdir="${classes.dir}/${ant.project.name}" classpathref="classpath" includeantruntime="false"/>\n'
    xmlstring += '</target>\n'
    xmlstring += '<target name="compile">\n'
    xmlstring += '<mkdir dir="${classes.dir}"/>\n'
    xmlstring += '<copy todir="${classes.dir}">\n'
    xmlstring += '<fileset dir="${src.dir}" excludes="**/*.java"/>\n'
    xmlstring += '</copy>\n'
    xmlstring += '<javac srcdir="${src.dir}" destdir="${classes.dir}" classpathref="classpath" includeantruntime="false"/>\n'
    xmlstring += '</target>\n'
    xmlstring += '<target name="jar-framework" depends="compile-framework">\n'
    xmlstring += '<jar destfile="${lib.dir}/${ant.project.name}/${ant.project.name}.jar" basedir="${classes.dir}/${ant.project.name}"/>\n'
    xmlstring += '</target>\n'
    xmlstring += '<target name="jar" depends="compile">\n'
    for app in apps_collection:
      xmlstring += '<mkdir dir="${jar.dir}/${'+app+'.name}"/>\n'
      xmlstring += '<jar destfile="${jar.dir}/${'+app+'.name}/${'+app+'.name}.jar" basedir="${classes.dir}"/>\n'
    xmlstring += '</target>\n'
    xmlstring += '<target name="war" depends="jar-framework,jar">\n'
    xmlstring += '<delete dir="${build.dir}/tmp"/>\n'
    xmlstring += '<mkdir dir="${build.dir}/tmp"/>\n'
    xmlstring += '<mkdir dir="${war.dir}"/>\n'
    for app in apps_collection:
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app+'.name}" preservelastmodified="true">\n'
      xmlstring += '<fileset dir="${classes.dir}/${ant.project.name}">\n'
      xmlstring += '<exclude name="**/*.java"/>\n'
      xmlstring += '<include name="**/**"/>\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app+'.name}" preservelastmodified="true">\n'
      xmlstring += '<fileset dir="${classes.dir}/${'+app+'.name}">\n'
      xmlstring += '<exclude name="**/*.java"/>\n'
      xmlstring += '<include name="**/**"/>\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app+'.name}/WEB-INF/lib" preservelastmodified="true" flatten="true">\n'
      xmlstring += '<fileset dir="${lib.dir}">\n'
      xmlstring += '<include name="**/*.jar" />\n'
      xmlstring += '<include name="**/*.zip" />\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<copy todir="${build.dir}/tmp/${'+app+'.name}/WEB-INF/lib" preservelastmodified="true" flatten="true">\n'
      xmlstring += '<fileset dir="${jar.dir}/${'+app+'.name}">\n'
      xmlstring += '<include name="**/*.jar" />\n'
      xmlstring += '<include name="**/*.zip" />\n'
      xmlstring += '</fileset>\n'
      xmlstring += '</copy>\n'
      xmlstring += '<jar destfile="${war.dir}/${'+app+'.name}.war" basedir="${build.dir}/tmp/${'+app+'.name}" />\n'
      xmlstring += '<delete dir="${jar.dir}/${'+app+'.name}"/>\n'
    xmlstring += '<delete dir="${build.dir}/tmp"/>\n'
    xmlstring += '</target>\n'
    xmlstring += '<target name="main" depends="clean,war">\n'
    xmlstring += '<echo>Congrats, you just built all your app(s)!</echo>\n'
    xmlstring += '</target>\n'
    xmlstring += '</project>\n'

    #write to build.xml and run ant...
    f = open('build.xml', 'w')
    f.write(xmlstring)
    f.close()
    if os.path.isfile('build.xml'):
      os.system('ant')
  else:
    print 'Oops! I did not recognize that command. Please try again.'

if app_arg == '' and buildall == False:
  print 'This script accepts two options.\n'
  print '1) To build a specific app in the apps directory, try: python othello.py --app=foo\n'
  print 'where foo is the directory name of your app.\n'
  print '2) To build all the apps in the apps directory, try: python othello.py --buildall\n'
