package mongo.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

import javax.mail.internet.InternetAddress;
import javax.mail.internet.AddressException;

import org.apache.commons.lang3.StringUtils;
import org.apache.log4j.*;

import com.google.gson.Gson;

import src.main.othello.web.controller.impl.AbstractControllerImpl;
import mongo.app.models.Encryption;
import mongo.app.models.MongoDB;

import com.mongodb.util.JSON;

import mongo.app.models.User;
import mongo.app.models.UserOid;

public class Auth extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Auth.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {

      if (request.getParameter("route").equals("login")) {
          this.login(request, response);
      } else if (request.getParameter("route").equals("register")) {
          this.register(request, response);
      }

  }

  public void login(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {

      String email = request.getParameter("email");
      String password = request.getParameter("password");

      if (StringUtils.isNotBlank(email)) {
          List<Object> results = new ArrayList();

          MongoDB mongo = new MongoDB();
          mongo.connect();
          mongo.getCollection("user");

          Map query = new HashMap();
          query.put("email", email);

          results = mongo.getDocuments(query);

          if (!results.isEmpty()) {

              String result = JSON.serialize(results.get(0));

              Gson gson = new Gson();

              User user = gson.fromJson(result, User.class);

              if (StringUtils.isNotBlank(user.getId())) {
                  Cookie userCookie = new Cookie("eleveny_user", user.getId());
                  response.addCookie(userCookie);
                  this.success(user, request, response);
              }

          } else {
              request.setAttribute("failed", true);
              super.forward("app/views/login.jsp", request, response);
          }

      } else {
          request.setAttribute("failed", true);
          super.forward("app/views/login.jsp", request, response);
      }

  }

  public void register(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {

      String email = request.getParameter("email");
      String fullname = request.getParameter("fullname");
      String password = request.getParameter("password");

      if (StringUtils.isNotBlank(email) && StringUtils.isNotBlank(fullname) && StringUtils.isNotBlank(password)) {

          if (validateEmail(email) == true && password.length() > 7) {

              List<String> indexNames = new ArrayList();
              indexNames.add("email");
              indexNames.add("fullname");

              Map document = new HashMap();
              document.put("email", email);
              document.put("fullname", fullname);
              document.put("status", 1);
              document.put("password", password);

              MongoDB mongo = new MongoDB();
              mongo.connect();
              mongo.getCollection("user");
              mongo.setIndex(indexNames);
              mongo.setDocument(document);

              request.setAttribute("registered", true);
              super.forward("app/views/login.jsp", request, response);

          } else if (validateEmail(email) == false) {
              request.setAttribute("bad_email", true);
              super.forward("app/views/register.jsp", request, response);
          } else if (password.length() < 8) {
              request.setAttribute("bad_password", true);
              super.forward("app/views/register.jsp", request, response);
          } else {
              request.setAttribute("failed", true);
              super.forward("app/views/register.jsp", request, response);
          }

      } else {
          request.setAttribute("failed", true);
          super.forward("app/views/register.jsp", request, response);
      }
  }

  public void success(User user, HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      String cookieValue = this.getCookieValue(request.getCookies(), "eleveny_user", "invalid");
      request.setAttribute("cookieValue", cookieValue);
      request.setAttribute("fullname", user.getName());
      request.setAttribute("email", user.getEmail());
      request.setAttribute("status", user.getStatus());
      request.setAttribute("created_at", user.getCreatedAt());
      super.forward("app/views/success.jsp", request, response);
  }

  public static String getCookieValue(Cookie[] cookies, String cookieName, String defaultValue) {
      for(Cookie cookie : cookies) {
          if (cookieName.equals(cookie.getName())) {
              return(cookie.getValue());
          }
      }
      return(defaultValue);
  }

  public static boolean validateEmail(String email) {

      try {
          new InternetAddress(email).validate();
      } catch (AddressException e) {
          logger.error(e.getMessage());
          return false;
      }
      return true;

  }

  public static String encrypt() {
      Encryption enc = new Encryption();
      String password = "P@ssW0rd";
      String encrypted = enc.encrypt(password);
      return encrypted;
  }


}
