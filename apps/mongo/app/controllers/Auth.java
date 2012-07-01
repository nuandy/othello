package mongo.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

import org.apache.commons.lang3.StringUtils;
import org.apache.log4j.*;

import com.google.gson.Gson;

import src.main.othello.web.controller.impl.AbstractControllerImpl;

import com.mongodb.util.JSON;

import mongo.app.models.User;
import mongo.app.models.UserOid;
import mongo.app.models.MongoDB;
import mongo.app.models.Util;

public class Auth extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger(Auth.class);

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {

      if (request.getParameter("route").equals("login")) {
          this.login(request, response);
      } else if (request.getParameter("route").equals("register")) {
          this.register(request, response);
      } else if (request.getParameter("route").equals("logout")) {
          this.logout(request, response);
      }

  }

  public Boolean allowed(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {

      String cookieValue = Util.getCookieValue(request.getCookies(), "myapptoken", "");

      List<Object> results = new ArrayList<Object>();

      MongoDB.connect();
      MongoDB.getCollection("user");

      Map query = new HashMap();
      query.put("auth_token", cookieValue);

      results = MongoDB.getDocuments(query);

      if (!results.isEmpty()) {

          String result = JSON.serialize(results.get(0));

          Gson gson = new Gson();
          User user = gson.fromJson(result, User.class);

          if (user.getAuthToken() != null) {
              return true;
          }

      }
      return false;

  }

  public void login(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {

      String email = request.getParameter("email");
      String password = request.getParameter("password");

      if (StringUtils.isNotBlank(email) && StringUtils.isNotBlank(password)) {
          List<Object> results = new ArrayList<Object>();

          MongoDB.connect();
          MongoDB.getCollection("user");

          Map query = new HashMap();
          query.put("email", email);
          query.put("password", password);

          results = MongoDB.getDocuments(query);

          if (!results.isEmpty()) {

              String result = JSON.serialize(results.get(0));

              Gson gson = new Gson();
              User user = gson.fromJson(result, User.class);

              if (StringUtils.isNotBlank(user.getId())) {
                  this.setUserCookie(user, request, response);
                  response.sendRedirect("success.jsp");
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

          if (Util.validateEmail(email) == true && password.length() > 7) {

              List<String> indexNames = new ArrayList<String>();
              indexNames.add("email");
              indexNames.add("fullname");

              Map document = new HashMap();
              document.put("email", email);
              document.put("fullname", fullname);
              document.put("status", 1);
              document.put("password", password);

              MongoDB.connect();
              MongoDB.getCollection("user");
              MongoDB.setIndex(indexNames);
              MongoDB.setDocument(document);

              request.setAttribute("registered", true);
              super.forward("app/views/login.jsp", request, response);

          } else if (Util.validateEmail(email) == false) {
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

  public void logout(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      Cookie userCookie = new Cookie("myapptoken", "");
      userCookie.setMaxAge(0);
      response.addCookie(userCookie);
      request.setAttribute("signedout", true);
      super.forward("app/views/login.jsp", request, response);
  }

  public static void setUserCookie(User user, HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      String data = Util.encryptCookie(user);

      Cookie userCookie = new Cookie("myapptoken", data);
      userCookie.setMaxAge(3600);
      response.addCookie(userCookie);

      Map document = new HashMap();
      document.put("status", user.getStatus());
      document.put("fullname", user.getName());
      document.put("email", user.getEmail());
      document.put("password", user.getPassword());
      document.put("created_at", user.getCreatedAt());
      document.put("auth_token", data);

      MongoDB.connect();
      MongoDB.getCollection("user");
      MongoDB.updateDocumentByEmail(user.getEmail(), document);
  }

}
