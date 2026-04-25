class commandLineArgument
{
    public static void main(String args[])
    {
        // If i want to take argument from command line we can : 
        // javac CommandLineArgument.java -> hit Enter
        // java CommandLineArgument "String1" "String2"
        System.out.println("Before converting to integer (concat of Strings) : " + args[0] + args[1]);
        // System.out.println(args[1]);

        // How to convert String to integer   ||
        // int a = Integer.parseInt(args[0]); ||
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        System.out.println("After converting to integer : " + (a + b));
    }
}