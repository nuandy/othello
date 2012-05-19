Othello is a Java MVC web framework.

Requirements: Java 6 (Othello incorporates Java 6 features)

Assuming Othello is installed under /web/othello.

To build all apps in the /web/othello/apps directory:

1. cd /web/othello
2. python bin/othello-build.py --buildall

To build a specific app named "test" in the /web/othello/apps directory:

1. cd /web/othello
2. python bin/othello-build.py --app=test

To tell the server which app to run:

1. cd /web/othello/contexts
2. Open context.xml
3. Replace "release/test.war" with "release/foo.war", where "foo.war" is the app you want to run.

To start the server:

1. cd /web/othello
2. python bin/othello-start.py

To start the server as a daemon on MAC OS X:

1. Place /web/othello/bin/othello.plist file in /Library/LaunchDaemons on MAC OS X
2. Run this command to load/start Othello's Jetty Server as a daemon: launchctl load /Library/LaunchDaemons/othello.plist
3. Run this command to unload/stop Othello's Jetty Server as a daemon: launchctl unload /Library/LaunchDaemons/othello.plist

I'm happy to answer any questions about Othello. Please send me an email at: nuandy@gmail.com.
