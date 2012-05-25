package mongo.app.models;

import java.net.UnknownHostException;
import java.util.Set;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

import com.mongodb.Mongo;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.BasicDBObject;
import com.mongodb.DBObject;
import com.mongodb.DBCursor;

import org.apache.log4j.*;


public class MongoDB {

    private static Logger logger = Logger.getLogger(MongoDB.class);

    public DB connect() throws UnknownHostException {
        Mongo m = new Mongo();
        DB db = m.getDB("mydb");
        return db;
    }

    public static String getCollectionNames(DB db) {
        String collections = "";
        Set<String> colls = db.getCollectionNames();

        for (String s : colls) {
            collections += s + ",";
        }

        return collections;
    }

    public static DBCollection getCollection(String name, DB db) {
        DBCollection collection = db.getCollection(name);
        return collection;
    }

    public static void createIndex(List<String> names, DBCollection collection) {
        for (String name : names) {
            collection.ensureIndex(new BasicDBObject(name, 1));
        }
    }

    public static void createDocument(List<Map<String, String>> data, DBCollection collection) {
        BasicDBObject dbObj = new BasicDBObject();

        for (Map<String, String> d : data) {
            for (Map.Entry<String, String> entry : d.entrySet()) {
                dbObj.put(entry.getKey(), entry.getValue());
            }
        }

        dbObj.put("created_at", (int) (System.currentTimeMillis()/1000));
        collection.insert(dbObj);
    }


}
