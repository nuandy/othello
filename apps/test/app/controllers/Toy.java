package test.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import org.apache.log4j.*;
import src.main.othello.web.controller.impl.AbstractControllerImpl;
import test.app.models.ToyToXml;
import test.app.models.XmlToToy;

public class Toy extends AbstractControllerImpl {

    private static Logger logger = Logger.getLogger(Toy.class);

    public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        ToyToXml.transform();
        String name = XmlToToy.transform();
        request.setAttribute("toyName", name);
        super.forward("app/views/toy.jsp", request, response);
    }

}

