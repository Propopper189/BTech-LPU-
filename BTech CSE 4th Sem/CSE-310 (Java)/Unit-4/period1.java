class period1
{
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        
        // Accept date in the form of String
        String s1 = sc.nextLine(); // Give input as : yyyy-MM-dd
        String s2 = sc.nextLine(); // Give input as : yyyy-MM-dd

        // Convert String into dates
        java.time.LocalDate date1 = java.time.LocalDate.parse(s1);
        java.time.LocalDate date2 = java.time.LocalDate.parse(s2);

        java.time.Period p = java.time.Period.between(date1, date2);
        System.out.println(p.getYears() + " Year " + p.getMonths() + " Month " + p.getDays() + " Days");
    }
}