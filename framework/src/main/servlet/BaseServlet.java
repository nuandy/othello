package src.main.servlet;

import java.util.regex.*;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import javax.servlet.*;
import javax.servlet.http.*;
import java.lang.reflect.Method;
import org.apache.log4j.*;

import java.io.File;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;


public class BaseServlet extends HttpServlet {

    private static Logger logger = Logger.getLogger("BaseServlet");

    public void service(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        invokeDo(request, response, request.getMethod().toUpperCase(), request.getServletPath());
    }

    public void invokeDo(HttpServletRequest request, HttpServletResponse response, String httpMethod, String pattern) throws IOException, ServletException {
        try {
            Class appController = Class.forName(getClassName(pattern));
            Method[] methods = appController.getMethods();
            Object object = appController.newInstance();
            for (Method method : methods) {
                if (method.getName().startsWith("do")) {
                    try {
                        method.invoke(object, request, response);
                    } catch (InvocationTargetException x) {
                        Throwable cause = x.getCause();
                        logger.error(cause.getMessage());
                    }
                }
            }
        } catch (Exception e) {
            logger.error(e);
        }
    }

    private String getClassName(String pattern) {

        String controller = "";
        String appKey = getServletContext().getInitParameter("app.key");

        try {

            File file = new File("apps/"+appKey+"/conf/routes.xml");
            JAXBContext jaxbContext = JAXBContext.newInstance(Routes.class);

            Unmarshaller jaxbUnmarshaller = jaxbContext.createUnmarshaller();
            Routes routes = (Routes) jaxbUnmarshaller.unmarshal(file);

            for (RouteURL u : routes.urls) {
                if (pattern.equals(u.url)) {
                    controller = u.controller;
                }
            }

            return controller;

        } catch (JAXBException e) {
            e.printStackTrace();
        }

        return controller;

    }
}
