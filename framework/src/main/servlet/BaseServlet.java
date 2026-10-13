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
        try {
            Class appController = Class.forName(getClassName(pattern));
            Method handler = findHandler(appController, httpMethod);
            if (handler == null) {
                response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED);
                return;
            }
            Object object = appController.newInstance();
            try {
                handler.invoke(object, request, response);
            } catch (InvocationTargetException ite) {
                Throwable cause = ite.getCause();
                logger.error(cause.getMessage());
            }
        } catch (Exception e) {
            logger.error(e);
        }
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
