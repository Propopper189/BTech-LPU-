enum Day
{
    MON, TUE, WED
}

class practice7
{
    public static void main(String args[])
    {

        // =====================================================
        // values()
        // Usage:
        // Returns all enum constants as an array
        // Mostly used in loops
        // =====================================================

        System.out.println("values():");

        for(Day d : Day.values())
        {
            System.out.println(d);
        }


        // =====================================================
        // ordinal()
        // Usage:
        // Returns index position of enum constant
        // Index starts from 0
        // =====================================================

        System.out.println("\nordinal():");

        System.out.println("MON = " + Day.MON.ordinal());
        System.out.println("TUE = " + Day.TUE.ordinal());


        // =====================================================
        // valueOf()
        // Usage:
        // Converts String into enum constant
        // String must exactly match enum name
        // =====================================================

        System.out.println("\nvalueOf():");

        Day d1 = Day.valueOf("WED");

        System.out.println(d1);


        // =====================================================
        // name()
        // Usage:
        // Returns enum constant name as String
        // =====================================================

        System.out.println("\nname():");

        System.out.println(Day.MON.name());


        // =====================================================
        // compareTo()
        // Usage:
        // Compares ordinal values
        // Positive -> greater
        // Negative -> smaller
        // Zero -> equal
        // =====================================================

        System.out.println("\ncompareTo():");

        System.out.println(Day.MON.compareTo(Day.WED));


        // =====================================================
        // equals()
        // Usage:
        // Checks whether two enum constants are same
        // Returns true or false
        // =====================================================

        System.out.println("\nequals():");

        System.out.println(Day.MON.equals(Day.MON));

        System.out.println(Day.MON.equals(Day.TUE));


        // =====================================================
        // toString()
        // Usage:
        // Converts enum constant into String
        // =====================================================

        System.out.println("\ntoString():");

        System.out.println(Day.TUE.toString());

    }
}