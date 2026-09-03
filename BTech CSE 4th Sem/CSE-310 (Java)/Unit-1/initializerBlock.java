class initializerBlock
{
    { // Initializer block -> gets executed before constructor.
        System.out.println("I am inside initializer block");
    }
    initializerBlock()
    { // Constructor -> gets called when an object is created
        System.out.println("I am inside constructor");
    }
    static
    { // static block -> gets executed before main function
        System.out.println("I am inside static block");
    }
    public static void main(String args[])
    {
        initializerBlock obj1 = new initializerBlock();
        System.out.println("I am inside main function");
        initializerBlock obj2 = new initializerBlock();
    }
}