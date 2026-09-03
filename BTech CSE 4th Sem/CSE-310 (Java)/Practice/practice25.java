import java.time.*;
import java.time.format.*;

// LocalDateTime Class

public class practice25 {
    public static void main(String args[])
    {
        String time = "15-05-2026 14:59:59";
        DateTimeFormatter f = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        LocalDateTime t = LocalDateTime.parse(time, f);
        System.out.println(t.getDayOfMonth() + " " + t.getMonth() + " " + t.getYear() + " " + t.getHour() + " " + t.getMinute() + " " + t.getSecond());
        System.out.println("After 5 Days : " + t.plusDays(5).format(f));
        System.out.println("After 21 Hours : " + t.plusHours(21).format(f));
    }   
}
