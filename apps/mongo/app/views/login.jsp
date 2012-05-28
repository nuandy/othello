<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<c:set var="just_registered" value="${registered}" />
<c:set var="signin_failed" value="${failed}" />

<html>
  <head>
    <title>Mongo App</title>
  </head>
  <body>

    <c:choose>
      <c:when test="${just_registered}">
        <h1>Great! You have succesfully registered as a member.</h1>
        <h1>Try to log in below.</h1>
      </c:when>
      <c:when test="${signin_failed}">
        <h1>Oops! We could not sign you in.</h1>
        <h1>Please check your credentials and try again.</h1>
      </c:when>
      <c:otherwise>
        <h1>Welcome!</h1>
      </c:otherwise>
    </c:choose>

    <h1>Sign in</h1>
    <form action="auth?route=login" method="post">
      <input type="text" name="email" placeholder="Email" />
      <input type="text" name="password" placeholder="Password" />
      <input type="submit" name="login" value="Log in" />
    </form>
    <p>Not a member? </p><a href="register">Register Now</a>
  </body>
</html>
