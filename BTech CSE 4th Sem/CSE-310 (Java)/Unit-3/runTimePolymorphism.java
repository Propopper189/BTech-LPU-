// Overriding
class A
{
    void lpu(int x)
    {
        System.out.println("Parent : " + x);
    }
}
class runTimePolymorphism extends A
{
    void lpu(int y)
    {
        // multiple inheritance is not supported in java
        
        super.lpu(y);
        System.out.println("Child : " + y); // overriden method
    }
    public static void main(String args[])
    {
        runTimePolymorphism obj = new runTimePolymorphism();
        obj.lpu(5); // child method will be called

        // note : assign child object to parent refernce to call the overriden method
        A objA = new runTimePolymorphism(); // A objA = parent reference
        objA.lpu(10);
    }
}