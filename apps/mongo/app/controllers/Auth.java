package mongo.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import org.apache.log4j.*;
import src.main.othello.web.controller.impl.AbstractControllerImpl;
import mongo.app.models.Encryption;
import mongo.app.models.MongoDB;

public class Auth extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Auth.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      MongoDB mongo = new MongoDB();
      mongo.getCollection("dude", mongo.connect());
      //String collectionNames = mongo.getCollectionNames(mongo.connect());
      //request.setAttribute("collectionNames", collectionNames);
      //super.forward("app/views/auth.jsp", request, response);
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
