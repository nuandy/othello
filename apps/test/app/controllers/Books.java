package test.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import org.apache.log4j.*;
import src.main.othello.web.controller.impl.AbstractControllerImpl;
import test.app.models.JerseyClientGet;

public class Books extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Books.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      JerseyClientGet.get();
      super.forward("app/views/books.jsp", request, response);
  }

}
