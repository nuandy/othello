package hello_world.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import org.apache.log4j.*;
import hello_world.app.models.UploadFiles;
import src.main.othello.web.controller.impl.AbstractControllerImpl;

public class Upload extends AbstractControllerImpl {

  private static Logger logger = Logger.getLogger("Upload");

  public static void initUpload(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      UploadFiles upf = new UploadFiles();
      upf.upload(request, response);
  }

  public void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      initUpload(request, response);
      super.forward("app/views/upload.jsp", request, response);
  }

}
