package hello_world.app.models;

import java.sql.*;
import java.text.*;
import java.io.*;
import org.apache.log4j.*;

public class Insert extends Jdbc {

    private static Logger logger = Logger.getLogger("Insert");

    Connection       db;
    Statement        sql;

    public void insert(String table, String column, String value) throws SQLException {
        db = Jdbc();
        sql = db.createStatement();
        String query = "insert into " + table + "(" + column + ") values (?)";
        PreparedStatement insertStatement = db.prepareStatement(query);
        insertStatement.setString(1, value);
        insertStatement.executeUpdate();
        db.close();
    }

}