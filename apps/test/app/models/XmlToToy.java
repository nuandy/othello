package test.app.models;

import org.apache.log4j.*;
import java.io.File;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;

public class XmlToToy {

    private static Logger logger = Logger.getLogger(XmlToToy.class);

    public static String transform() {

        String name = "";

        try {

            File file = new File("apps/test/toy.xml");
            JAXBContext jaxbContext = JAXBContext.newInstance(Toy.class);

            Unmarshaller jaxbUnmarshaller = jaxbContext.createUnmarshaller();
            Toy toy = (Toy) jaxbUnmarshaller.unmarshal(file);
            name = toy.name;
            return name;

        } catch (JAXBException e) {
            e.printStackTrace();
        }

        return name;

    }
}
