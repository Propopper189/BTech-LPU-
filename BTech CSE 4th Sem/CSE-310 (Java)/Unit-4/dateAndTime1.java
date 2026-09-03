class dateAndTime1
{
    // These are pre defined classes : (present inside "java.time.*")
    // LocalDate
    // LocalTime
    // LocalDateTime
    // Period (find the difference between 2 dates).
    // Duration (find the difference between 2 times).
    public static void main(String args[])
    {
        // Write a program to print the current system date.
        java.time.LocalDate d1 = java.time.LocalDate.now();
        System.out.println("The date today is : " + d1);

        // Create a custom date
        java.time.LocalDate d2 = java.time.LocalDate.of(2021, 02, 24); // YYYY-MM-DD
        System.out.println("The custom date is : " + d2);

        // Write a program to print the current year, month and date separately
        java.time.LocalDate d3 = java.time.LocalDate.now();
        System.out.println("The year is : " + d3.getYear());
        System.out.println("The month is : " + d3.getMonth());
        System.out.println("The date is : " + d3.getDayOfMonth());
        System.out.println("The day is : " + d3.getDayOfWeek());
        System.out.println("Today is " + d3.getDayOfYear() + "th day of the year");
    }
}