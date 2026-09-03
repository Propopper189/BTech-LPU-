

class dateAndTime3
{
    // Write a program to accept a date from the user and print it
    public static void main(String[] args)
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        
        // This is one method : 

        // int date = sc.nextInt();
        // int month = sc.nextInt();
        // int year = sc.nextInt();
        // java.time.LocalDate d = java.time.LocalDate.of(year, month, date);
        // System.out.println("Date : " + d);
    
        // This is another method : 
        // Convert string to date

        String s = "2026-03-21"; // yyyy-MM-dd
        java.time.LocalDate d = java.time.LocalDate.parse(s);
        java.time.format.DateTimeFormatter f = java.time.format.DateTimeFormatter.ofPattern("dd-MMMM-yyyy");
        System.out.println("Date entered by the user is : " + d.format(f));
    }
}