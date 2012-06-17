package mongo.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import mongo.app.controllers.Auth;

import org.apache.log4j.*;
import src.main.othello.web.controller.impl.AbstractControllerImpl;

public class Success extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Success.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      Auth auth = new Auth();
      if (auth.allowed(request, response) == true) {
          super.forward("app/views/success.jsp", request, response);
      } else {
          super.forward("app/views/login.jsp", request, response);
      }
  }

}

