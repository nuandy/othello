import os
import sys

"""owfbuildf.py by Andy Nu nuandy@gmail.com
Builds the Othello framework. Try: python owfbuildf.py
"""

xml_version = '1.0'
encoding = 'UTF-8'

path = os.path.realpath('.')
base = os.path.basename(path)

def touch(fname, times = None):
  with file(fname, 'a'):
    os.utime(fname, times)

if base == 'othello':
  xmlstring =  '<?xml version="' + xml_version + '" encoding="' + encoding  + '" ?>\n'
  xmlstring += '<project name="othello" basedir="." default="main">\n'
  xmlstring += '<property name="build.compiler" value="org.eclipse.jdt.core.JDTCompilerAdapter"/>\n'
  xmlstring += '<property name="othello.dir" value="framework"/>\n'
  xmlstring += '<property name="lib.dir"     value="lib"/>\n'
  xmlstring += '<property name="build.dir"   value="build"/>\n'
  xmlstring += '<property name="classes.dir" value="${build.dir}/classes"/>\n'
  xmlstring += '<property name="war.dir"     value="release"/>\n'
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
  xmlstring += '<javac source="1.6" target="1.6" srcdir="${othello.dir}" destdir="${classes.dir}/${ant.project.name}" classpathref="classpath" includeantruntime="false" compiler="org.eclipse.jdt.core.JDTCompilerAdapter"/>\n'
  xmlstring += '</target>\n'
  xmlstring += '<target name="jar-framework" depends="compile-framework">\n'
  xmlstring += '<mkdir dir="${lib.dir}/${ant.project.name}"/>\n'
  xmlstring += '<jar destfile="${lib.dir}/${ant.project.name}/${ant.project.name}.jar" basedir="${classes.dir}/${ant.project.name}"/>\n'
  xmlstring += '</target>\n'
  xmlstring += '<target name="main" depends="clean,jar-framework">\n'
  xmlstring += '<echo>Congrats, you just built the Othello framework!</echo>\n'
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
  sys.exit("Oops! This script must be run within the root/top level othello directory!")
