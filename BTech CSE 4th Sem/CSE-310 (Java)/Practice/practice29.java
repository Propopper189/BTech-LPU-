import java.time.*;
import java.time.format.*;
public class practice29 {
    public static void main(String args[])
    {
        String time1 = "08:15:10 PM";
        String time2 = "10:15:20 PM";
        DateTimeFormatter f = DateTimeFormatter.ofPattern("hh:mm:ss a");
        LocalTime t1 = LocalTime.parse(time1, f);
        LocalTime t2 = LocalTime.parse(time2, f);
        Duration d = Duration.between(t1, t2);
        System.out.println(d.toHours());
        System.out.println(d.toMinutes());
        System.out.println(d.toSeconds());
    }
}
