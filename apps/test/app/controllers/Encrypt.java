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
      Encryption enc = new Encryption();
      String password = "l1nSan1ty";
      String encrypted = enc.encrypt(password);
      request.setAttribute("encrypted", encrypted);
      super.forward("app/views/encrypt.jsp", request, response);
  }

}
