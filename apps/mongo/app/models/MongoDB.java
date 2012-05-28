package mongo.app.models;

import java.net.UnknownHostException;
import java.util.Set;
import java.util.List;
import java.util.ArrayList;
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

    private static DB db = null;
    private static DBCollection collection = null;

    public static void connect() throws UnknownHostException {
        Mongo m = new Mongo();
        db = m.getDB("mydb");
    }

    public static void getCollection(String name) {
        collection = db.getCollection(name);
    }

    public static void setIndex(List<String> names) {
        for (String name : names) {
            collection.ensureIndex(new BasicDBObject(name, 1));
        }
    }

    public static void setDocument(Map<String, ?> data) {
        BasicDBObject dbObj = new BasicDBObject();

        for (Map.Entry<String, ?> entry : data.entrySet()) {
            dbObj.put(entry.getKey(), entry.getValue());
        }

        dbObj.put("created_at", (int) (System.currentTimeMillis()/1000));
        collection.insert(dbObj);
    }

    public static List<Object> getDocuments(Map<String, ?> data) {

	      List<Object> results = new ArrayList();

	      BasicDBObject query = new BasicDBObject();

        for (Map.Entry<String, ?> entry : data.entrySet()) {
            query.put(entry.getKey(), entry.getValue());
        }

        DBCursor cursor = collection.find(query);

        while(cursor.hasNext()) {
            results.add(cursor.next());
        }

	      return results;
    }

    public static List<String> getCollectionNames(DB db) {
        List<String> collections = new ArrayList();
        Set<String> colls = db.getCollectionNames();

        for (String s : colls) {
            collections.add(s);
        }

        return collections;
    }

}
