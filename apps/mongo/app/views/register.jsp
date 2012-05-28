<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<html>
  <head>
    <title>Mongo App</title>
  </head>
  <body>
    <h1>Register</h1>
    <form action="auth?route=register" method="post">
      <input type="text" name="fullname" placeholder="Full Name" />
      <input type="text" name="email" placeholder="Email" />
      <input type="text" name="password" placeholder="Password" />
      <input type="submit" name="register" value="Register" />
    </form>
  </body>
</html>
