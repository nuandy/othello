<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<jsp:include page="includes/header.jsp" />

<c:set var="authorized" value="${cookieValue}" />

<c:choose>
  <c:when test="${authorized}">
    <h1>Results of your query:</h1>
    <p>Name: ${fullname}</p>
    <p>Email: ${email}</p>
    <p>Status: ${status}</p>
    <p>Created At: ${created_at}</p>
    <h1>Cookie Value</h1>
    <p>${cookieValue}</p>
  </c:when>
  <c:otherwise>
    <h1>Oops! You must <a href="login">sign in</a> to view this page.</h1>
  </c:otherwise>
</c:choose>

<jsp:include page="includes/footer.jsp" />
