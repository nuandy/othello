<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<jsp:include page="includes/header.jsp" />

<c:set var="registration_failed" value="${failed}" />
<c:set var="bad_email" value="${bad_email}" />
<c:set var="bad_password" value="${bad_password}" />

<c:choose>
  <c:when test="${registration_failed}">
    <h1>Oops! We could not complete registration.</h1>
    <h1>Please make sure all fields are filled in.</h1>
  </c:when>
  <c:when test="${bad_email}">
    <h1>Oops! We could not complete registration.</h1>
    <h1>The email you provided is invalid.</h1>
  </c:when>
  <c:when test="${bad_password}">
    <h1>Oops! We could not complete registration.</h1>
    <h1>Your password must be at least 8 characters long.</h1>
  </c:when>
  <c:otherwise>
    <h1>Welcome to My App!</h1>
  </c:otherwise>
</c:choose>

<div class="register">

  <h1>Register</h1>

  <form action="auth?route=register" method="post">
    <input type="text" name="fullname" placeholder="Full Name" />
    <input type="text" name="email" placeholder="Email" />
    <input type="password" name="password" placeholder="Password" />
    <input type="submit" name="register" value="Register" />
  </form>

  <p>Already a member? <a href="login">Sign in now</a></p>

</div>

<jsp:include page="includes/footer.jsp" />
