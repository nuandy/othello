package test.app.models;

import org.apache.log4j.*;
import org.jasypt.util.text.BasicTextEncryptor;

public class Encryption {

    private static Logger logger = Logger.getLogger(Encryption.class);

    public static String encrypt() {

        String text = "The quick brown fox jumps over the lazy dog";
        BasicTextEncryptor bte = new BasicTextEncryptor();
        bte.setPassword("HelloWorld");
        String encrypted = bte.encrypt(text);
        String original = bte.decrypt(encrypted);
        return encrypted;

    }
}

