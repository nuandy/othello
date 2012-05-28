package mongo.app.models;

public class User {

    UserOid _id;
    int status;
    String email;
    String password;
    String fullname;
    int created_at;

    public String getId() {
        return _id.getOid();
    }

    public String getName() {
        return fullname;
    }

    public String getEmail() {
        return email;
    }

    public int getStatus() {
        return status;
    }

    public int getCreatedAt() {
        return created_at;
    }

}
