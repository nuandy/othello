package test.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import org.apache.log4j.*;
import src.main.othello.web.controller.impl.AbstractControllerImpl;

public class Test extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger("Test");

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      super.forward("app/views/test.jsp", request, response);
  }

}
