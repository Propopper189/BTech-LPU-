class A
{
    int x = 5;
    A(int a)
    {
        System.out.println(a);
    }
    void display()
    {
        System.out.println("Class A : display");
    }
}
class inheritance4 extends A
{
    int x = 6;
    inheritance4(int a)
    {
        super(a);
    }
    void display()
    {
        System.out.println(super.x + this.x);
        // super class -> parent class -> "super" keyword is 
        // used to access attributes of parent class
        super.display();
    }
    // inheritance4() 
    // {
    //     System.out.println("Inheritance4");
    // }
    public static void main(String args[])
    {
        inheritance4 obj = new inheritance4(120);
        obj.display();
    }
    
}