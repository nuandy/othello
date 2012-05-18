Othello is a Java MVC web framework.

Requirements: Java 6 (Othello incorporates Java 6 features)

Assuming Othello is installed under /web/othello.

To build all apps in the /web/othello/apps directory:

1. cd /web/othello
2. python othello.py --buildall

To build a specific app named "hello_world" in the /web/othello/apps directory:

1. cd /web/othello
2. python othello.py --app=hello_world

To tell the server which app to run:

1. cd /web/othello/contexts
2. Open context.xml
3. Replace "release/hello_world.war" with "release/foo.war", where "foo.war" is the app you want to run.

To start the server:

1. cd /web/othello
2. ./bin/othello.sh

I'm happy to answer any questions about Othello. Please send me an email at: nuandy@gmail.com.
