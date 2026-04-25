// Write a program to print the date which will come after 10 days
class dateAndTime2
{
    public static void main(String[] args) 
    {
        java.time.LocalDate d1 = java.time.LocalDate.now();
        System.out.println("Date after 10 days will be : " + d1.plusDays(10));
        System.out.println("Date before 10 days will be : " + d1.minusDays(10)); 

        // Write a program to print the current system date, but the output must be in dd-MM-yyyy format
        
        // import java.time.format.*;  
        java.time.format.DateTimeFormatter f = java.time.format.DateTimeFormatter.ofPattern("dd-MMMM-yyyy");
        // java.time.format.DateTimeFormatter f = java.time.format.DateTimeFormatter.ofPattern("dd/MMMM/yyyy");
        // java.time.format.DateTimeFormatter f = java.time.format.DateTimeFormatter.ofPattern("dd-MMM-yyyy");
        // java.time.format.DateTimeFormatter f = java.time.format.DateTimeFormatter.ofPattern("dd-MM-yyyy");
        
        // mm => minutes || MM => Months || MMM => Mar/Apr/May... etc || MMMM => March/April/May/June.. etc
    
        System.out.println(d1.format(f));
    }
}