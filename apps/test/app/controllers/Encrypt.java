package test.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import org.apache.log4j.*;
import src.main.othello.web.controller.impl.AbstractControllerImpl;
import test.app.models.Encryption;

public class Encrypt extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Encrypt.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      String password = "P@ssW0rd";
      String encrypted = Encryption.encrypt(password);
      request.setAttribute("encrypted", encrypted);
      super.forward("app/views/encrypt.jsp", request, response);
  }

}
