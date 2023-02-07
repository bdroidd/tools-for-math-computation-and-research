//
// Alphabetizer.java
//
// This program creates a new array of items, then 
// orders them alphabetically.
//_________________________________________

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Alphabetizer 

{
    public static void  main(String[] args)
    {
        // creates a new list
        List <String> list = new ArrayList<>();

        // adds items to defined list (in this context, types of analytic spaces)
        list.add("Q_k");
        list.add("Morrey");
        list.add("rigid");
        list.add("Berkovich");
        list.add("partially");
        list.add("Archimedean/non-Archimedean");
        list.add("normal/quasi-normal");
        list.add("smooth/non-smooth");
        list.add("p-adic");
        list.add("hyperbolic");

        // displays list to user
        System.out.println(list);

        // orders items in list alphabetically
        Collections.sort(list, String.CASE_INSENSITIVE_ORDER);

        // displays now ordered list to user
        System.out.println("The items, ordered, are stated below.");
        System.out.println(list);

    }
    
}
