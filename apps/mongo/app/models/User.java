package mongo.app.models;

public class User {

    UserOid _id;
    int status;
    String email;
    String password;
    String fullname;
    String auth_token;
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

    public String getPassword() {
        return password;
    }

    public String getAuthToken() {
        return auth_token;
    }

    public int getCreatedAt() {
        return created_at;
    }

}
