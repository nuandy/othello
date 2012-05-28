package mongo.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

import org.apache.log4j.*;
import src.main.othello.web.controller.impl.AbstractControllerImpl;

public class Login extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Login.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      super.forward("app/views/login.jsp", request, response);
  }

}

