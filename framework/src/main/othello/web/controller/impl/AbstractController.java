package src.main.othello.web.controller.impl;

import src.main.othello.web.controller.Controller;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * src.main.othello.web.controller.impl
 * Author: Chris Hicks
 * Date: 11/19/11
 * Time: 10:32 AM
 */
public class AbstractController implements Controller {
    public void forward(String jsp, HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        RequestDispatcher view = request.getRequestDispatcher("app/views/upload.jsp");
        view.forward(request, response);
    }
}
