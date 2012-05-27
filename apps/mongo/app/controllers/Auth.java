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
import mongo.app.models.Encryption;
import mongo.app.models.MongoDB;

public class Auth extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Auth.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {	

      List<Object> results = new ArrayList();

      List<String> indexNames = new ArrayList();
      indexNames.add("email");
      indexNames.add("fullname");
      
      Map document = new HashMap();
      document.put("email", "nuandy@gmail.com");
      document.put("fullname", "Andy Nu");
      document.put("status", 1);

      Map query = new HashMap();
      query.put("status", 1);

      MongoDB mongo = new MongoDB();
      mongo.connect();
      mongo.getCollection("dude");
      mongo.setIndex(indexNames);
      mongo.setDocument(document);
      results = mongo.getDocuments(query);

      request.setAttribute("results", results);
      super.forward("app/views/auth.jsp", request, response);
  }

  public static void login() {

  }

  public static void register() {

  }

  public static String encrypt() {
      Encryption enc = new Encryption();
      String password = "P@ssW0rd";
      String encrypted = enc.encrypt(password);
      return encrypted;
  }


}
