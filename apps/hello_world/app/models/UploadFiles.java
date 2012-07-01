package hello_world.app.models;

import java.io.*;
import java.util.List;
import java.util.Iterator;
import javax.servlet.*;
import javax.servlet.http.*;
import hello_world.app.models.Insert;
import org.apache.log4j.*;
import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.FileUploadException;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;

public class UploadFiles {

    private static Logger logger = Logger.getLogger(UploadFiles.class);

    public static void upload(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        boolean isMultipart = ServletFileUpload.isMultipartContent(request);

        if (!isMultipart) {

        } else {
            DiskFileItemFactory fileItemFactory = new DiskFileItemFactory ();
            fileItemFactory.setSizeThreshold(1*1024*1024); //1 MB
            ServletFileUpload uploadHandler = new ServletFileUpload(fileItemFactory);
            List items = null;
            try {
                items = uploadHandler.parseRequest(request);
            } catch (FileUploadException e) {
                logger.error(e);
            }
            Iterator itr = items.iterator();
            while (itr.hasNext()) {
                FileItem item = (FileItem) itr.next();
                if (item.isFormField()) {
                } else {
                    try {
                        String itemName = item.getName();
                        if (itemName.length() > 0) {
                            File savedFile = File.createTempFile("hello-", ".jpg", new File(System.getProperty("user.dir")+"/apps/hello_world/app/public/images"));
                            item.write(savedFile);
                            Insert sql = new Insert();
                            sql.insert("images", "image_path", savedFile.getPath());
                        }
                    } catch (Exception e) {
                        logger.error(e);
                    }
                }
            }
        }
    }
}
