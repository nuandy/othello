package test.app.models;

import org.apache.log4j.*;
import java.io.File;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;

public class ToyToXml {

    private static Logger logger = Logger.getLogger(ToyToXml.class);

    public static void transform() {

        Toy toy = new Toy();
        toy.setId(1);
        toy.setName("Soul of Chogokin Voltes V GX-31 Diecast Robot");
        toy.setBrand("Bandai");

        try {
            File file = new File("apps/test/toy.xml");
            JAXBContext jaxbContext = JAXBContext.newInstance(Toy.class);
            Marshaller jaxbMarshaller = jaxbContext.createMarshaller();

            jaxbMarshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            jaxbMarshaller.marshal(toy, file);

        } catch (JAXBException e) {
            logger.error(e);
        }

    }
}
