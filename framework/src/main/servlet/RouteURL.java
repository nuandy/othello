package src.main.servlet;

import javax.xml.bind.annotation.*;

public class RouteURL {

    @XmlAttribute
    String controller;

    @XmlValue
    String url;

}
