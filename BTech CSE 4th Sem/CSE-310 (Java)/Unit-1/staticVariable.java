class staticVariable
{
/*
1. Any variable preceded by the keyword static is called as static variable
2. static variable creates a single memory and that will be shared by all the objects
    of the class and if any object changes the value of the static variable then that 
    changed value will be reflected in all other objects.
3. If static variable is not initialized then it will be initialized to 0 automatically.
*/
    int a;
    static int b; 
    staticVariable() 
    {
        a = 5;
        b = 6;
    }
    void get()
    {
        a++;
        b++;
    }
    void display()
    {
        System.out.println("A : " + (a));
        System.out.println("B : " + b);
    }
    public static void main(String arg[])
    {
        staticVariable obj1 = new staticVariable();
        staticVariable obj2 = new staticVariable();
        obj1.get();
        System.out.println("Object 1");
        obj1.display();
        System.out.println("Object 2");
        obj2.display();
    }
}