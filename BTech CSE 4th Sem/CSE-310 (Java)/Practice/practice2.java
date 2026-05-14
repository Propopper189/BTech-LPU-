class practice2 
{
    /*
        Primitive Data Types
        int 4 bytes
        double 8 bytes
        char 2 bytes
        boolean true/false
        float 4 bytes
        long 8 bytes
        short 2 bytes
        byte 1 byte
    */
   public static void main(String[] args) {
        int a = 10;
        double b = a;
        int c = (int) b;
        Integer d = c;
        int e  = d.intValue();
        double f = Double.parseDouble("6");
        System.out.println(a + " " + b + " " + c + " " + d + " " + e + " " + f);
   }
}
