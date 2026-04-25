//WAp to accept a date and print it falls in weekend or weekday 

import java.time.*;
import java.util.*;

class A 
{
    public static void main(String arg[])
    {
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        //convert string to date 
        LocalDate d=LocalDate.parse(s);
       // System.out.println(d.getDayOfWeek());
       DayOfWeek day=d.getDayOfWeek();
       if(day==day.SUNDAY || day==day.SATURDAY)
       {
           System.out.println("WeekEnd");
       }
       else
       {
           System.out.println("WeekDay");
       }
        
    }
}