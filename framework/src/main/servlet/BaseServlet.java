package src.main.servlet;

import java.io.IOException;
import javax.servlet.*;
import javax.servlet.http.*;
import java.lang.reflect.Method;
import org.apache.log4j.*;

public class BaseServlet extends HttpServlet {

    private Logger logger = Logger.getLogger(this.getClass().getName());

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
                    method.invoke(object, request, response);
                }
            }
        } catch (Exception e) {
            logger.warn(e);
        }
    }

    public static String capitalizeFirstLetters(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (i == 0) {
                s = String.format("%s%s", Character.toUpperCase(s.charAt(0)), s.substring(1));
            }
            if (!Character.isLetterOrDigit(s.charAt(i))) {
                if (i + 1 < s.length()) {
                    s = String.format("%s%s%s", s.subSequence(0, i+1), Character.toUpperCase(s.charAt(i + 1)), s.substring(i+2));
                }
            }
        }
        return s;
    }

    private String getClassName(String pattern) {
        String appKey = getServletContext().getInitParameter("app.key");
        String servletName = pattern.replace("/","");
        String servletNameCaps = capitalizeFirstLetters(servletName);
        String controllerName = servletNameCaps.replace("_","").replace(".","").replace("-","");
        return appKey+".app.controllers."+controllerName;
    }

}
