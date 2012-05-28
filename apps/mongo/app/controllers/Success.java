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

public class Success extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Success.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      super.forward("app/views/success.jsp", request, response);
  }

}

