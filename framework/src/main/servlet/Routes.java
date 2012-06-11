package src.main.servlet;

import java.util.*;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name="routes")
public class Routes {

    @XmlElement(name="url")
    List<RouteURL> urls=new ArrayList<RouteURL>();

}
