package mongo.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

import mongo.app.controllers.Auth;

import org.apache.log4j.*;
import src.main.othello.web.controller.impl.AbstractControllerImpl;

public class Login extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Login.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      Auth auth = new Auth();
      if (auth.allowed(request, response) == true) {
          super.forward("app/views/success.jsp", request, response);
      } else {
          super.forward("app/views/login.jsp", request, response);
      }
  }

}
