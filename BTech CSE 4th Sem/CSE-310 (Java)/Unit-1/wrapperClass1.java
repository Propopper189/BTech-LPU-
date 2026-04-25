class wrapperClass1
{
    // 1. Auto - Boxing
    //  -> concerting data type to wrapper class
    //  -> automatic
    //  -> int a = 5;
    //  -> Integer b = a; (automatic)
    //  -> System.out.println(b);
    
    // 2. Unboxing
    //  -> automatic
    //  -> Integer x = 5;
    //  -> int y = x; (automatic)
    //  -> System.out.println(y);

    public static void main(String[] args) {
        // Auto - Boxing (converting pdt to wrapper class)
        int a = 5;
        Integer b = a;
        System.out.println(b);

        // Unboxing (converting wrapper class to pdt)
        Integer x = 6;
        int y = x;
        System.out.println(y);
    }
}