package src.main.othello.web.controller;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * src.main.othello.web.controller
 * Author: Chris Hicks
 * Date: 11/19/11
 * Time: 10:29 AM
 */
public interface Controller {
    public void forward(String jsp, HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException;
}
