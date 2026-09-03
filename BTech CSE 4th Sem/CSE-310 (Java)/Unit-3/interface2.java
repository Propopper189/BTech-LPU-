/*
Interface : 
    Can contain 3 types of methods : 
        1. static methods. (doesn't require objects to access static method)
        2. default methods. (require objects)
        3. abstract methods.
        4. Variables
    
    Note : A method (without body) inside interface is by default abstract.
*/

interface a
{
    int x = 10;
    void abc(); // By Default public and abstract method as there is no body 
    // (by default in interface but have to write the abstract keyword in abstract class for making it an abstract method)
    static void xyz() // Static method
    {
        System.out.println("Static method called");
    }
    default void mno() // Default Method
    {
        System.out.println("Default method called");
        System.out.println("variable x : " + x);
    }
}
class interface2 implements a
{
    @Override
    public void abc()
    {
        System.out.println("Overriden Method Called");
    }
    public static void main(String args[])
    {
        a obj = new interface2();
        obj.abc();
        obj.mno(); // default method can be called by the object
        a.xyz(); // static methods can be called by class name directly without creating objects.
    }
}