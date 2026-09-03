// Static block is always executed prior to void main()
class staticBlock1
{
    // Static block -> gets executed before main function,
    // no matter in which order we write the main and static block
    // (Only 1 static block)
    public static void main(String args[])
    {
        // Java is dynamic in nature (at the runtime one java program can link with another java program because of public)
        // Because of "static" keyword the main function does not require any object for its access
        System.out.println("I am in main function");
    }
    static
    {
        System.out.println("I am in static block");
    }
}