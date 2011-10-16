#!/bin/bash
java -DSTART=$PWD/server/start.config -jar $PWD/server/start.jar $PWD/server/config/jetty.xml
