import os
import sys

"""othello.py by Andy Nu nuandy@gmail.com
This script will create a build.xml file and build all the app(s)
contained in the othello/apps directory using ant.
"""

version = '1.0'
encoding = 'utf-8'

def listapps():
  apps = [name for name in os.listdir('.') if os.path.isdir(name)]
  return apps

xmlstring =  '<?xml version="' + version + '" encoding="' + encoding  + '" ?>\n'
xmlstring += '<project name="othello" basedir="." default="main">\n'
xmlstring += '<property name="othello.dir" value="framework"/>\n'
xmlstring += '<property name="src.dir"     value="apps"/>\n'
xmlstring += '<property name="lib.dir"     value="lib"/>\n'
xmlstring += '<property name="build.dir"   value="build"/>\n'
xmlstring += '<property name="classes.dir" value="${build.dir}/classes"/>\n'
xmlstring += '<property name="jar.dir"     value="release"/>\n'
xmlstring += '<property name="war.dir"     value="release"/>\n'

os.chdir(sys.path[0]+'/apps')
for name in listapps():
  xmlstring += '<property name="'+name+'.dir"    value="apps/'+name+'"/>\n'
  xmlstring += '<property name="'+name+'.name"   value="'+name+'"/>\n'
os.chdir(sys.path[0])

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
os.chdir(sys.path[0]+'/apps')
for name in listapps():
  xmlstring += '<mkdir dir="${jar.dir}/${'+name+'.name}"/>\n'
  xmlstring += '<jar destfile="${jar.dir}/${'+name+'.name}/${'+name+'.name}.jar" basedir="${classes.dir}"/>\n'
os.chdir(sys.path[0])
xmlstring += '</target>\n'

xmlstring += '<target name="war" depends="jar-framework,jar">\n'
xmlstring += '<delete dir="${build.dir}/tmp"/>\n'
xmlstring += '<mkdir dir="${build.dir}/tmp"/>\n'
xmlstring += '<mkdir dir="${war.dir}"/>\n'

os.chdir(sys.path[0]+'/apps')
for name in listapps():
  xmlstring += '<copy todir="${build.dir}/tmp/${'+name+'.name}" preservelastmodified="true">\n'
  xmlstring += '<fileset dir="${classes.dir}/${ant.project.name}">\n'
  xmlstring += '<exclude name="**/*.java"/>\n'
  xmlstring += '<include name="**/**"/>\n'
  xmlstring += '</fileset>\n'
  xmlstring += '</copy>\n'
  xmlstring += '<copy todir="${build.dir}/tmp/${'+name+'.name}" preservelastmodified="true">\n'
  xmlstring += '<fileset dir="${classes.dir}/${'+name+'.name}">\n'
  xmlstring += '<exclude name="**/*.java"/>\n'
  xmlstring += '<include name="**/**"/>\n'
  xmlstring += '</fileset>\n'
  xmlstring += '</copy>\n'
  xmlstring += '<copy todir="${build.dir}/tmp/${'+name+'.name}/WEB-INF/lib" preservelastmodified="true" flatten="true">\n'
  xmlstring += '<fileset dir="${lib.dir}">\n'
  xmlstring += '<include name="**/*.jar" />\n'
  xmlstring += '<include name="**/*.zip" />\n'
  xmlstring += '</fileset>\n'
  xmlstring += '</copy>\n'
  xmlstring += '<copy todir="${build.dir}/tmp/${'+name+'.name}/WEB-INF/lib" preservelastmodified="true" flatten="true">\n'
  xmlstring += '<fileset dir="${jar.dir}/${'+name+'.name}">\n'
  xmlstring += '<include name="**/*.jar" />\n'
  xmlstring += '<include name="**/*.zip" />\n'
  xmlstring += '</fileset>\n'
  xmlstring += '</copy>\n'
  xmlstring += '<jar destfile="${war.dir}/${'+name+'.name}.war" basedir="${build.dir}/tmp/${'+name+'.name}" />\n'
  xmlstring += '<delete dir="${jar.dir}/${'+name+'.name}"/>\n'
os.chdir(sys.path[0])

xmlstring += '<delete dir="${build.dir}/tmp"/>\n'
xmlstring += '</target>\n'

xmlstring += '<target name="main" depends="clean,war">\n'
xmlstring += '<echo>Congrats, you just built your app(s)!</echo>\n'
xmlstring += '</target>\n'

xmlstring += '</project>\n'

f = open('build.xml', 'w')
f.write(xmlstring)
f.close()
if os.path.isfile('build.xml'):
  os.system('ant')
