class dateAndTime4
{
    public static void main(String args[])
    {
        // Write a program to print the current system time
        java.time.LocalTime t = java.time.LocalTime.now(java.time.ZoneId.of("Asia/Kolkata"));
        java.time.format.DateTimeFormatter f = java.time.format.DateTimeFormatter.ofPattern("hh:mm");
        System.out.println(t.format(f));
    }
}