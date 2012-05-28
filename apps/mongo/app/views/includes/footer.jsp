<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>

    <ul>
      <li><a href="success">Home</a></li>
      <li>|</li>
      <c:choose>
        <c:when test="${fn:length(cookie.eleveny_user.value) > 0}">
          <li><a href="auth?route=logout">Sign out</a></li>
        </c:when>
        <c:otherwise>
          <li><a href="login">Sign in</a></li>
        </c:otherwise>
      </c:choose>
      <li>|</li>
      <li><a href="register">Register</a></li>
      <li>&copy; 2012 My App Powered By Othello Web Framework</li>
    </ul>

  </body>

</html>
