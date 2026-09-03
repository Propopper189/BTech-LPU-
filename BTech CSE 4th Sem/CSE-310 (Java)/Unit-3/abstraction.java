abstract class student
{
    abstract void abc(); // Abstract Method

    int a = 10; // Variable

    student() // Constructor
    {
        System.out.println("Constructor Called");
    }
    void xyz() // Non Abstract Method
    {
        System.out.println("This is non abstract method");
        System.out.println("The value of a is : " + a);
    }
}
class abstraction extends  student
{
    // Abstraction : using some sort of things without knowing its background details
    // (Hiding the implementation of details from the user and only showing the output)
    
    // Note : abstraction can be acheived in 2 ways : 
    // 1. Abstract class
    // 2. interface

    // 1. Abstract class :
    // =====================
    // a class preceded by abstract keyword is called as abstract class.
    // Example : 
    // abstract class student {}
    
    // what abstract class contains ?
    // 1. can contain abstract method, which does not have any body
    // 2. can contain non abstract method
    // 3. can contain constructors
    // 4. can contain variables

    // Note : We don't create an object of abstract class

    @Override // Note : The class which extends to abstract class must override all the abstract method.
    public void abc() // This was abstract method in parent class
    {
        System.out.println("Overriden Method called");
    }
    public static void main(String[] args) 
    {
        student obj = new abstraction(); // student -> parent and abstraction -> child
        obj.abc();
        obj.xyz();
    }
}