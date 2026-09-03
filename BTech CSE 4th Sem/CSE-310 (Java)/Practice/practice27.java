import java.time.*;
import java.time.format.*;

public class practice27 {
    public static void main(String args[])
    {
        // LocalDateTime stores only date and time
        // It does not store timezone information
        LocalDateTime t = LocalDateTime.now();

        // Adding timezone to LocalDateTime
        ZonedDateTime zd =
        t.atZone(ZoneId.of("Asia/Kolkata"));

        // Formatter
        DateTimeFormatter f =
        DateTimeFormatter.ofPattern(
        "dd-MM-yyyy hh:mm:ss a");

        // Printing formatted ZonedDateTime
        System.out.println(
        zd.format(f));

        // Printing hour in 24-hour format
        System.out.println(
        "Hour : " + zd.getHour());
    }
}

/*
Alternative Method

import java.time.*;
import java.time.format.*;

public class practice27 {
    public static void main(String args[])
    {
        // Directly creating ZonedDateTime
        ZonedDateTime zd =
        ZonedDateTime.now(
        ZoneId.of("Asia/Kolkata"));

        DateTimeFormatter f =
        DateTimeFormatter.ofPattern(
        "dd-MM-yyyy hh:mm:ss a");

        System.out.println(
        zd.format(f));

        System.out.println(
        "Hour : " + zd.getHour());
    }
}
*/