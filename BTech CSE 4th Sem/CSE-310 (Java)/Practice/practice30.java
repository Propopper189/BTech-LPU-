import java.time.*;
import java.time.format.*;
public class practice30 {
    public static void main(String args[])
    {
        // Input is "15-May-2026"
        String date = "15-May-2026";
        DateTimeFormatter f = DateTimeFormatter.ofPattern("dd-MMM-yyyy");
        LocalDate dt1 = LocalDate.parse(date, f);
        f = DateTimeFormatter.ofPattern("dd-MMMM-yyyy");
        System.out.println(dt1.format(f));
        System.out.println(dt1.getDayOfWeek());
        System.out.println(dt1.plusDays(40).format(f));
    }
}
