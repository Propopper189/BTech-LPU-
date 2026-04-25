class objectOfMain
{
    // int a = 5;
    void lpu() // function definition
    {
        System.out.println("I am in LPU");
    }
    public static void main(String args[])
    {
        // Main obj = new Main(); // obj -> Object reference ; Object created with "new Main()"
        new objectOfMain().lpu();
        // System.out.println(obj.a);
        // obj.lpu(); // function declaration (when the system reaches the function declaration, the function is called).
        // obj.lpu();
    }
}