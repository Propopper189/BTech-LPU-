
import java.time.LocalDateTime;

// Write a program to accept a date and time and add 5 days and 2 hours.
class practice13
{
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s = "12-03-2026 10:15";
        java.time.format.DateTimeFormatter f = java.time.format.DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm");
        java.time.LocalDateTime d = java.time.LocalDateTime.parse(s, f);
        LocalDateTime dt = d.plusDays(5).plusHours(2);
        System.out.println(dt.format(f));
    }
}