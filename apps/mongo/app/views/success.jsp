<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>

<jsp:include page="includes/header.jsp" />

<c:choose>
  <c:when test="${fn:length(cookie.eleveny_user.value) > 0}">
    <h1>My App</h1>
    <p>User Name: ${cookie.eleveny_user_name.value}</p>
    <p>User Email: ${cookie.eleveny_user_email.value}</p>
    <p>User ID: ${cookie.eleveny_user.value}</p>
  </c:when>
  <c:otherwise>
    <c:redirect url="/login" />
  </c:otherwise>
</c:choose>

<jsp:include page="includes/footer.jsp" />
