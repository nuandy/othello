package hello_world.app.controllers;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import org.apache.log4j.*;
import hello_world.app.models.UploadFiles;

public class Upload {

  private static Logger logger = Logger.getLogger("Upload");

  public static void initUpload(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      UploadFiles upf = new UploadFiles();
      upf.upload(request, response);
  }

  public static void doMain(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
      initUpload(request, response);
      RequestDispatcher view = request.getRequestDispatcher("app/views/upload.jsp");
      view.forward(request, response);
  }

}
