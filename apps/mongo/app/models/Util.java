package mongo.app.models;

import javax.servlet.http.*;

import javax.mail.internet.InternetAddress;
import javax.mail.internet.AddressException;

import mongo.app.models.Encryption;

import org.apache.log4j.*;

public class Util {

    private static Logger logger = Logger.getLogger(Util.class);

    public static String getCookieValue(Cookie[] cookies, String cookieName, String defaultValue) {
        for(Cookie cookie : cookies) {
            if (cookieName.equals(cookie.getName())) {
                return(cookie.getValue());
            }
        }
        return defaultValue;
    }

    public static boolean validateEmail(String email) {

        try {
            new InternetAddress(email).validate();
        } catch (AddressException e) {
            logger.error(e.getMessage());
            return false;
        }
        return true;

    }

    public static String encryptCookie(User user) {
        String data = user.getId() + (System.currentTimeMillis()/1000);
        String encrypted = Encryption.encrypt(data);
        return encrypted;
    }

}
