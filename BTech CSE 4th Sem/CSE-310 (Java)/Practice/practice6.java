public class practice6 {
    // VarArgs
    // Varargs (Variable Arguments) in Java allow a method to accept:
    // Any number of arguments
    // Syntax : datatype ... variableName

    static void summision(int ... x)
    {
        int sum = 0;
        for(int i = 0; i < x.length; i++)
        {
            sum += x[i];
        }
        System.out.println(sum);
    }
    public static void main(String args[])
    {
        practice6.summision(1);
    }
}
