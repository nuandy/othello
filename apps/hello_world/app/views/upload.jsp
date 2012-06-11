<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<html>
  <head>
    <title>File Uploader</title>
  </head>
  <body>
    <form action="upload.jsp" method="post" enctype="multipart/form-data" name="upload_form">
      <p>Choose file: <input name="file1" type="file"></p>
      <p>Choose file: <input name="file2" type="file"></p>
      <p>Choose file: <input name="file3" type="file"></p>
      <p><input type="submit" name="upload_form_submit" value="Upload Files"></p>
    </form>
  </body>
</html>
