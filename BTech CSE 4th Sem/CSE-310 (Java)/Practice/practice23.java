// LocalDate Class
import java.time.*;
import java.time.format.*;
public class practice23 
{
    public static void main(String args[])
    {
        String date = "15-05-2026";
        DateTimeFormatter f = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate d = LocalDate.parse(date, f);
        System.out.println("Date : " + d.getDayOfMonth());
        System.out.println("After 5 Days : Date : " + d.plusDays(5));
        System.out.println("After 5 Months : Date : " + d.plusMonths(5));
        System.out.println("After 5 Years : Date : " + d.plusYears(5));
        System.out.println("Day : " + d.getDayOfWeek()); 
        System.out.println("Month : " + d.getMonth()); 
        System.out.println("Month : " + d.getMonthValue()); 
        System.out.println("Year : " + d.getYear());
        System.out.println("Is Leap ? : " + d.isLeapYear());
    }
}
