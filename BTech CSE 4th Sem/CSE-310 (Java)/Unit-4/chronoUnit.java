// Write a program to accept 2 dates and find the difference between these two dates in terms of number of days.
class chronoUnit
{
    public static void main(String args[])
    {
        // class : ChronoUnit | package : java.time.temporal
        java.util.Scanner sc = new java.util.Scanner(System.in);
        
        // Accept date in the form of String
        String s1 = sc.nextLine(); // Give input as : yyyy-MM-dd
        String s2 = sc.nextLine(); // Give input as : yyyy-MM-dd
        java.time.LocalDate date1 = java.time.LocalDate.parse(s1);
        java.time.LocalDate date2 = java.time.LocalDate.parse(s2);
        long numOfDays = java.time.temporal.ChronoUnit.DAYS.between(date1, date2);
        System.out.println("Number of days : " + numOfDays);
        long m = java.time.temporal.ChronoUnit.MONTHS.between(date1, date2);
        long y = java.time.temporal.ChronoUnit.YEARS.between(date1, date2);
        System.out.println("Number of months : " + m);
        System.out.println("Number of years : " + y);
    }
}