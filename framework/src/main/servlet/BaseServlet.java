package src.main.servlet;

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

    private static final long serialVersionUID = 37L;

    private static Logger logger = Logger.getLogger("BaseServlet");

    public void service(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        invokeDo(request, response, request.getMethod().toUpperCase(), request.getServletPath());
    }

    public void invokeDo(HttpServletRequest request, HttpServletResponse response, String httpMethod, String pattern) throws IOException, ServletException {
        String className = getClassName(pattern);
        if (className.length() == 0) {
            response.sendError(HttpServletResponse.SC_NOT_FOUND);
            return;
        }

        Class<?> appController;
        try {
            appController = Class.forName(className);
        } catch (ClassNotFoundException e) {
            throw fail("Controller " + className + " for " + pattern + " was not found", e);
        }

        Method handler = findHandler(appController, httpMethod);
        if (handler == null) {
            response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED);
            return;
        }

        try {
            handler.invoke(appController.newInstance(), request, response);
        } catch (InvocationTargetException ite) {
            // Rethrow what the controller threw, so the container answers 500 and shows the app's error page.
            Throwable cause = ite.getCause();
            logger.error(className + "." + handler.getName() + " failed for " + pattern, cause);
            if (cause instanceof IOException) {
                throw (IOException) cause;
            }
            if (cause instanceof ServletException) {
                throw (ServletException) cause;
            }
            if (cause instanceof RuntimeException) {
                throw (RuntimeException) cause;
            }
            if (cause instanceof Error) {
                throw (Error) cause;
            }
            throw new ServletException(cause);
        } catch (InstantiationException e) {
            throw fail("Controller " + className + " could not be created", e);
        } catch (IllegalAccessException e) {
            throw fail("Controller " + className + " could not be created", e);
        }
    }

    private ServletException fail(String message, Throwable cause) {
        logger.error(message, cause);
        return new ServletException(message, cause);
    }

    // A controller handles a request with do<Method> (doGet, doPost, ...) when it has one, otherwise with doMain.
    static Method findHandler(Class<?> controller, String httpMethod) {
        String specific = "do" + httpMethod.substring(0, 1) + httpMethod.substring(1).toLowerCase();
        for (String name : new String[] {specific, "doMain"}) {
            try {
                return controller.getMethod(name, HttpServletRequest.class, HttpServletResponse.class);
            } catch (NoSuchMethodException e) {
                // try the next name
            }
        }
        return null;
    }

    private String getClassName(String pattern) throws ServletException {

        String controller = "";
        String appKey = getServletContext().getInitParameter("app.key");
        File file = new File("apps/"+appKey+"/conf/routes.xml");

        try {

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
            throw fail("Could not read routes from " + file.getAbsolutePath(), e);
        }

    }
}
