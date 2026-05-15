import java.time.*;
import java.time.format.*;
import java.time.temporal.*;

public class practice28 {
    public static void main(String args[])
    {
        String date1 = "15-05-2026";
        String date2 = "18-06-2028";
        DateTimeFormatter f = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate dt1 = LocalDate.parse(date1, f);
        LocalDate dt2 = LocalDate.parse(date2, f);
        Period p = Period.between(dt1, dt2);
        System.out.println("Days (not the exact gap): " + p.getDays());
        System.out.println("Months (not the exact gap) : " + p.getMonths());
        System.out.println("Years (not the exact years) : " + p.getYears());
        System.out.println("Days (Exact Number of Days) : " + ChronoUnit.DAYS.between(dt1, dt2));
        System.out.println("Months (Exact Number of Months) : " + ChronoUnit.MONTHS.between(dt1, dt2));
        System.out.println("Years (Exact Number of Years) : " + ChronoUnit.YEARS.between(dt1, dt2));
    }
}
