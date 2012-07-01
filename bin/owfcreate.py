import os
import sys
import getopt

xml_version = '1.0'
encoding = 'UTF-8'
app_key = ''

options, extraparams = getopt.getopt(sys.argv[1:], '', ['app='])

path = os.path.realpath('.')
base = os.path.basename(path)

def createapp():
  if base == 'othello':
    for opt, arg in options:
      if opt in ('--app'):
        app_key = arg
        os.mkdir(os.path.abspath(os.curdir)+'/apps/'+app_key,0777)
        os.chdir(os.path.abspath(os.curdir)+'/apps/'+app_key)
        os.mkdir('WEB-INF',0777)
        os.chdir('WEB-INF')
        xmlstring = '<?xml version="' + xml_version + '" encoding="' + encoding  + '" ?>\n'
        xmlstring += '<web-app xmlns="http://java.sun.com/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" metadata-complete="true" version="2.5">\n'
        xmlstring += '<display-name>' + app_key + ' app</display-name>\n'
        xmlstring += '<session-config>\n'
        xmlstring += '<session-timeout>20</session-timeout>\n'
        xmlstring += '</session-config>\n'
        xmlstring += '<servlet>\n'
        xmlstring += '<servlet-name>default</servlet-name>\n'
        xmlstring += '<servlet-class>org.mortbay.jetty.servlet.DefaultServlet</servlet-class>\n'
        xmlstring += '<init-param>\n'
        xmlstring += '<param-name>dirAllowed</param-name>\n'
        xmlstring += '<param-value>false</param-value>\n'
        xmlstring += '</init-param>\n'
        xmlstring += '<init-param>\n'
        xmlstring += '<param-name>welcomeServlets</param-name>\n'
        xmlstring += '<param-value>true</param-value>\n'
        xmlstring += '</init-param>\n'
        xmlstring += '</servlet>\n'
        xmlstring += '<welcome-file-list>\n'
        xmlstring += '<welcome-file>index.jsp</welcome-file>\n'
        xmlstring += '</welcome-file-list>\n'
        xmlstring += '<servlet>\n'
        xmlstring += '<servlet-name>BaseServlet</servlet-name>\n'
        xmlstring += '<servlet-class>src.main.servlet.BaseServlet</servlet-class>\n'
        xmlstring += '</servlet>\n'
        xmlstring += '<context-param>\n'
        xmlstring += '<description>Unique App Key</description>\n'
        xmlstring += '<param-name>app.key</param-name>\n'
        xmlstring += '<param-value>' + app_key + '</param-value>\n'
        xmlstring += '</context-param>\n'
        xmlstring += '<error-page>\n'
        xmlstring += '<error-code>404</error-code>\n'
        xmlstring += '<location>/app/views/http_status/404.html</location>\n'
        xmlstring += '</error-page>\n'
        xmlstring += '<error-page>\n'
        xmlstring += '<error-code>500</error-code>\n'
        xmlstring += '<location>/app/views/http_status/500.html</location>\n'
        xmlstring += '</error-page>\n'
        xmlstring += '</web-app>\n'
        f = open('web.xml', 'w')
        f.write(xmlstring)
        f.close()
        os.chdir(os.path.pardir)
        os.mkdir('app',0777)
        os.mkdir('conf',0777)
        os.chdir('conf')
        xmlstring = '<?xml version="' + xml_version + '" encoding="' + encoding  + '" ?>\n'
        xmlstring += '<routes>\n'
        xmlstring += '<url controller="'+ app_key  +'.app.controllers.Index">/index.jsp</url>\n'
        xmlstring += '</routes>\n'
        f = open('routes.xml', 'w')
        f.write(xmlstring)
        f.close()
        os.chdir(os.path.pardir)
        os.chdir('app')
        os.mkdir('public',0777)
        os.chdir('public')
        os.mkdir('js',0777)
        os.mkdir('css',0777)
        os.chdir(os.path.pardir)
        os.mkdir('controllers',0777)
        os.chdir('controllers')
        javastring = 'package '+app_key+'.app.controllers;\n'
        javastring += 'import java.io.*;\n'
        javastring += 'import javax.servlet.*;\n'
        javastring += 'import javax.servlet.http.*;\n'
        javastring += 'import java.util.Date;\n'
        javastring += 'import java.text.DateFormat;\n'
        javastring += 'import java.text.SimpleDateFormat;\n'
        javastring += 'import org.apache.log4j.*;\n'
        javastring += 'import src.main.othello.web.controller.impl.AbstractControllerImpl;\n'
        javastring += 'public class Index extends AbstractControllerImpl {\n'
        javastring += 'private static Logger logger = Logger.getLogger(Index.class);\n'
        javastring += 'public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {\n'
        javastring += 'DateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss");\n'
        javastring += 'Date date = new Date();\n'
        javastring += 'request.setAttribute("date", date);\n'
        javastring += 'super.forward("app/views/index.jsp", request, response);\n'
        javastring += '}\n'
        javastring += '}\n'
        f = open('Index.java', 'w')
        f.write(javastring)
        f.close()
        os.chdir(os.path.pardir)
        os.mkdir('models',0777)
        os.mkdir('views',0777)
        os.chdir('views')
        jspstring = '<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>\n'
        jspstring += '<html>\n'
        jspstring += '<head>\n'
        jspstring += '<title>'+ app_key +'</title>\n'
        jspstring += '</head>\n'
        jspstring += '<body>\n'
        jspstring += '<h1>Welcome to '+ app_key +'.</h1>\n'
        jspstring += '<h2>This app is powered by Othello!</h2>\n'
        jspstring += '<p>${date}</p>\n'
        jspstring += '</body>\n'
        jspstring += '</html>\n'
        f = open('index.jsp', 'w')
        f.write(jspstring)
        f.close()
        os.mkdir('http_status',0777)
        os.chdir('http_status')
        htmlstring = '<html>\n'
        htmlstring += '<head>\n'
        htmlstring += '<title>404 Page Not Found</title>\n'
        htmlstring += '</head>\n'
        htmlstring += '<body>\n'
        htmlstring += '<h1>Oops!</h1>\n'
        htmlstring += '<h2>We could not find that page you were trying to reach.</h2>\n'
        htmlstring += '<h3>Please check the URL and try again.</h3>\n'
        htmlstring += '<h4>You can always go back to our <a href="/">home page</a>.</h4>\n'
        htmlstring += '</body>\n'
        htmlstring += '</html>\n'
        f = open('404.html', 'w')
        f.write(htmlstring)
        f.close()
        htmlstring = '<html>\n'
        htmlstring += '<head>\n'
        htmlstring += '<title>500 Internal Server Error</title>\n'
        htmlstring += '</head>\n'
        htmlstring += '<body>\n'
        htmlstring += '<h1>Oops!</h1>\n'
        htmlstring += '<h2>We are sorry but something went wrong.</h2>\n'
        htmlstring += '<h3>We cannot serve any pages to you at this time.</h3>\n'
        htmlstring += '<h4>Please try again later.</h4>\n'
        htmlstring += '</body>\n'
        htmlstring += '</html>\n'
        f = open('500.html', 'w')
        f.write(htmlstring)
        f.close()
        print 'An app named '+app_key+' has been created.'
  elif base == 'bin':
    for opt, arg in options:
      if opt in ('--app'):
        app_key = arg
        os.mkdir(os.path.pardir+'/apps/'+app_key,0777)
        os.chdir(os.path.pardir+'/apps/'+app_key)
        os.mkdir('WEB-INF',0777)
        os.chdir('WEB-INF')
        xmlstring = '<?xml version="' + xml_version + '" encoding="' + encoding  + '" ?>\n'
        xmlstring += '<web-app xmlns="http://java.sun.com/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" metadata-complete="true" version="2.5">\n'
        xmlstring += '<display-name>' + app_key + ' app</display-name>\n'
        xmlstring += '<session-config>\n'
        xmlstring += '<session-timeout>20</session-timeout>\n'
        xmlstring += '</session-config>\n'
        xmlstring += '<servlet>\n'
        xmlstring += '<servlet-name>default</servlet-name>\n'
        xmlstring += '<servlet-class>org.mortbay.jetty.servlet.DefaultServlet</servlet-class>\n'
        xmlstring += '<init-param>\n'
        xmlstring += '<param-name>dirAllowed</param-name>\n'
        xmlstring += '<param-value>false</param-value>\n'
        xmlstring += '</init-param>\n'
        xmlstring += '<init-param>\n'
        xmlstring += '<param-name>welcomeServlets</param-name>\n'
        xmlstring += '<param-value>true</param-value>\n'
        xmlstring += '</init-param>\n'
        xmlstring += '</servlet>\n'
        xmlstring += '<welcome-file-list>\n'
        xmlstring += '<welcome-file>index.jsp</welcome-file>\n'
        xmlstring += '</welcome-file-list>\n'
        xmlstring += '<servlet>\n'
        xmlstring += '<servlet-name>BaseServlet</servlet-name>\n'
        xmlstring += '<servlet-class>src.main.servlet.BaseServlet</servlet-class>\n'
        xmlstring += '</servlet>\n'
        xmlstring += '<context-param>\n'
        xmlstring += '<description>Unique App Key</description>\n'
        xmlstring += '<param-name>app.key</param-name>\n'
        xmlstring += '<param-value>' + app_key + '</param-value>\n'
        xmlstring += '</context-param>\n'
        xmlstring += '<error-page>\n'
        xmlstring += '<error-code>404</error-code>\n'
        xmlstring += '<location>/app/views/http_status/404.html</location>\n'
        xmlstring += '</error-page>\n'
        xmlstring += '<error-page>\n'
        xmlstring += '<error-code>500</error-code>\n'
        xmlstring += '<location>/app/views/http_status/500.html</location>\n'
        xmlstring += '</error-page>\n'
        xmlstring += '</web-app>\n'
        f = open('web.xml', 'w')
        f.write(xmlstring)
        f.close()
        os.chdir(os.path.pardir)
        os.mkdir('app',0777)
        os.mkdir('conf',0777)
        os.chdir('conf')
        xmlstring = '<?xml version="' + xml_version + '" encoding="' + encoding  + '" ?>\n'
        xmlstring += '<routes>\n'
        xmlstring += '<url controller="'+ app_key  +'.app.controllers.Index">/index.jsp</url>\n'
        xmlstring += '</routes>\n'
        f = open('routes.xml', 'w')
        f.write(xmlstring)
        f.close()
        os.chdir(os.path.pardir)
        os.mkdir('public',0777)
        os.chdir('public')
        os.mkdir('js',0777)
        os.mkdir('css',0777)
        os.chdir(os.path.pardir)
        os.chdir('app')
        os.mkdir('controllers',0777)
        os.chdir('controllers')
        javastring = 'package '+app_key+'.app.controllers;\n'
        javastring += 'import java.io.*;\n'
        javastring += 'import javax.servlet.*;\n'
        javastring += 'import javax.servlet.http.*;\n'
        javastring += 'import java.util.Date;\n'
        javastring += 'import java.text.DateFormat;\n'
        javastring += 'import java.text.SimpleDateFormat;\n'
        javastring += 'import org.apache.log4j.*;\n'
        javastring += 'import src.main.othello.web.controller.impl.AbstractControllerImpl;\n'
        javastring += 'public class Index extends AbstractControllerImpl {\n'
        javastring += 'private static Logger logger = Logger.getLogger(Index.class);\n'
        javastring += 'public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {\n'
        javastring += 'DateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss");\n'
        javastring += 'Date date = new Date();\n'
        javastring += 'request.setAttribute("date", date);\n'
        javastring += 'super.forward("app/views/index.jsp", request, response);\n'
        javastring += '}\n'
        javastring += '}\n'
        f = open('Index.java', 'w')
        f.write(javastring)
        f.close()
        os.chdir(os.path.pardir)
        os.mkdir('models',0777)
        os.mkdir('views',0777)
        os.chdir('views')
        jspstring = '<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>\n'
        jspstring += '<html>\n'
        jspstring += '<head>\n'
        jspstring += '<title>'+ app_key +'</title>\n'
        jspstring += '</head>\n'
        jspstring += '<body>\n'
        jspstring += '<h1>Welcome to '+ app_key +'.</h1>\n'
        jspstring += '<h2>This app is powered by Othello!</h2>\n'
        jspstring += '<p>${date}</p>\n'
        jspstring += '</body>\n'
        jspstring += '</html>\n'
        f = open('index.jsp', 'w')
        f.write(jspstring)
        f.close()
        os.mkdir('http_status',0777)
        os.chdir('http_status')
        htmlstring = '<html>\n'
        htmlstring += '<head>\n'
        htmlstring += '<title>404 Page Not Found</title>\n'
        htmlstring += '</head>\n'
        htmlstring += '<body>\n'
        htmlstring += '<h1>Oops!</h1>\n'
        htmlstring += '<h2>We could not find that page you were trying to reach.</h2>\n'
        htmlstring += '<h3>Please check the URL and try again.</h3>\n'
        htmlstring += '<h4>You can always go back to our <a href="/">home page</a>.</h4>\n'
        htmlstring += '</body>\n'
        htmlstring += '</html>\n'
        f = open('404.html', 'w')
        f.write(htmlstring)
        f.close()
        htmlstring = '<html>\n'
        htmlstring += '<head>\n'
        htmlstring += '<title>500 Internal Server Error</title>\n'
        htmlstring += '</head>\n'
        htmlstring += '<body>\n'
        htmlstring += '<h1>Oops!</h1>\n'
        htmlstring += '<h2>We are sorry but something went wrong.</h2>\n'
        htmlstring += '<h3>We cannot serve any pages to you at this time.</h3>\n'
        htmlstring += '<h4>Please try again later.</h4>\n'
        htmlstring += '</body>\n'
        htmlstring += '</html>\n'
        f = open('500.html', 'w')
        f.write(htmlstring)
        f.close()
        print 'An app named '+app_key+' has been created.'
  else:
    sys.exit("Oops! This script must be run within the root/top level othello directory or othello/bin!")

createapp()
