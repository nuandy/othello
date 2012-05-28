<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>

<jsp:include page="includes/header.jsp" />

  <h1>My App</h1>
  <p>You are viewing this page because you have signed in successfully!</p>
  <p>Auth Token: ${cookie.myapptoken.value}</p>
  <p><a href="auth?route=logout">Sign Out</a></p>

<jsp:include page="includes/footer.jsp" />
