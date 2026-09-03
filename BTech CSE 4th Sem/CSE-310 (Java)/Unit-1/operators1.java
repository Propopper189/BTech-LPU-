class operators1
{
    /*
    1. Unary operator (one operand)
        -> ++, --, etc
    2. Binary operator
        -> +, -, *, /, ...etc
    3. Ternary operator
        -> ?
    */
   /*
    1. Arithmatic operator
        -> +, -, *, /
    2. Modular operator
        -> to find the remainder
    3. Assignment operator 
        -> =, +=, -=, *=, /=
    4. Relational operator (Conditional)
        -> <, >, ==, !=, >=, <=, .... etc
   */
    public static void main(String args[])
    {
        int a = 5;
        int b = 6;
        int max = (a>b) ? a : b;
        System.out.println(max);
        boolean c = (a>b);
        System.out.println(c);
    }
}