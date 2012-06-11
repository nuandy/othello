<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>

<jsp:include page="includes/header.jsp" />

<c:set var="just_registered" value="${registered}" />
<c:set var="signin_failed" value="${failed}" />
<c:set var="signed_out" value="${signedout}" />

<c:choose>
  <c:when test="${just_registered}">
    <h1>Great! You have succesfully registered as a member.</h1>
    <h1>Try to log in below.</h1>
  </c:when>
  <c:when test="${signin_failed}">
    <h1>Oops! We could not sign you in.</h1>
    <h1>Please check your credentials and try again.</h1>
  </c:when>
  <c:when test="${signed_out}">
    <h1>You have signed out. Hope to see you back soon.</h1>
  </c:when>
  <c:otherwise>
    <h1>Welcome to My App!</h1>
  </c:otherwise>
</c:choose>

<div class="login">

  <h1>Sign in</h1>

  <form action="auth.jsp?route=login" method="post">
    <input type="text" name="email" placeholder="Email" />
    <input type="password" name="password" placeholder="Password" />
    <input type="submit" name="login" value="Log in" />
  </form>

  <p>Not a member? <a href="register.jsp">Register now</a></p>

</div>

<jsp:include page="includes/footer.jsp" />
