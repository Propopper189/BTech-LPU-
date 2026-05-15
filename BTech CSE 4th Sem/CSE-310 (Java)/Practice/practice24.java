import java.time.*;
import java.time.format.*;

class practice24
{
    public static void main(String args[])
    {
        // String time = "02:30:20 PM";

        DateTimeFormatter f = DateTimeFormatter.ofPattern("hh:mm:ss a");

        LocalTime t = LocalTime.now();

        System.out.println("Time : " + t.format(f));

        System.out.println("Hour : " + t.getHour());
        System.out.println("After 4 Hours : Hour : " + (t.plusHours(4)).format(f));

        System.out.println("Minute : " + t.getMinute());

        System.out.println("Second : " + t.getSecond());
    }
}