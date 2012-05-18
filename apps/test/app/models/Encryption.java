package test.app.models;

import org.apache.log4j.*;
import org.jasypt.util.text.BasicTextEncryptor;

public class Encryption {

    private static Logger logger = Logger.getLogger(Encryption.class);

    public static String encrypt(String password) {

        BasicTextEncryptor bte = new BasicTextEncryptor();
        bte.setPassword("knicks");
        String encrypted = bte.encrypt(password);
        String original = bte.decrypt(encrypted);
        return encrypted;

    }
}
