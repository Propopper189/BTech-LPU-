enum Day
{
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}
class important
{
    public static void main(String args[])
    {
        Day d = Day.FRIDAY;
        System.out.println(d);
        for(Day day : Day.values())
        {
            System.out.print(day + " ");
        }
    }
}