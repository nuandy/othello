package test.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import org.apache.log4j.*;
import src.main.othello.web.controller.impl.AbstractControllerImpl;

public class Index extends AbstractControllerImpl {

    private static Logger logger = Logger.getLogger(Index.class);

    public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        request.setAttribute("test", "dude");
        super.forward("app/views/index.jsp", request, response);
    }

}
