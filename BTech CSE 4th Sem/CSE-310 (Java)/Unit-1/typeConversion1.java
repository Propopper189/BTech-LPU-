// Converting one data type to another data type is called as  type conversion.
// 1. Converting lower data type to higher data type is automatic. (type conversion)
//    int a = 53; 
//    double b = a; -> Implicit type conversion (automatic)
// 2. Converting higher data type to lower data type (Type casting)
//    double c = 52.94;
//    int d = (int) c; -> type casting -> d = 52 -> explicit type conversion
class typeConversion1
{
    public static void main(String args[])
    {
        int a = 53;
        double b = a; // implicit type conversion
        System.out.println(b);

        double c = 52.93;
        int d = (int) c; // Explicit type conversion (Casting)
        System.out.println(d);

        // Convert char to int
        char ch = 'a';
        int p = ch;
        System.out.println(p); // Ans: 97

        // Convert int to char
        int m = 65;
        char n = (char) m; // Explicit type conversion (casting)
        System.out.println(n); // Ans: A
    }
}