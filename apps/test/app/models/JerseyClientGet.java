package test.app.models;

import org.apache.log4j.*;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

public class JerseyClientGet {

    private static Logger logger = Logger.getLogger(JerseyClientGet.class);

    public static void get() {

        try {
            Client client = Client.create();

            WebResource webResource = client.resource("https://www.googleapis.com/books/v1/volumes?q=dragondoom");

            ClientResponse response = webResource.accept("application/json").get(ClientResponse.class);

            if (response.getStatus() != 200) {
                throw new RuntimeException("Failed : HTTP error code : " + response.getStatus());
            }

            String output = response.getEntity(String.class);

            logger.warn("Output from Server .... \n");
            logger.warn(output);

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
