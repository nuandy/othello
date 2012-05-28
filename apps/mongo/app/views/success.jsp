<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<html>
  <head>
    <title>Mongo App</title>
  </head>
  <body>
    <h1>Results of your query:</h1>
    <p>Name: ${fullname}</p>
    <p>Email: ${email}</p>
    <p>Status: ${status}</p>
    <p>Created At: ${created_at}</p>
    <h1>Cookie Value</h1>
    <p>${cookieValue}</p>
  </body>
</html>
