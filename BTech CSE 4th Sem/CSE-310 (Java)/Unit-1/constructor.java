class constructor
{
    int a;
    constructor() // Constructor; No return type; It automatically gets called when an object of the class is created. 
    {
        System.out.println("I am inside Constructor");
    }
    public static void main(String args[])
    {
        constructor obj = new constructor();
        // new Constructor();
        obj.a = 12;
        System.out.println(obj.a);
    }
}