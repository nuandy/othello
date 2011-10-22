package hello_world.app.models;

import java.sql.*;
import org.apache.log4j.*;

public class Jdbc {

    private static Logger logger = Logger.getLogger("Jdbc");

    public static Connection Jdbc() {
        try {
            Class.forName("org.postgresql.Driver");
		} catch (ClassNotFoundException e) {
            logger.warn("PostgreSQL JDBC Driver Missing");
		    e.printStackTrace();
		}
 
        logger.warn("PostgreSQL JDBC Driver Registered"); 
		
        Connection connection = null;
 
		try {
            connection = DriverManager.getConnection("jdbc:postgresql://127.0.0.1:5432/my_database_name", "username", "password");
        } catch (SQLException e) {
            logger.warn("Connection Failed");
		    e.printStackTrace();
		}
 
		if (connection != null) {
            logger.warn("Connected");
		} else {
            logger.warn("Not Connected");
		}
        return connection;
	}
}
