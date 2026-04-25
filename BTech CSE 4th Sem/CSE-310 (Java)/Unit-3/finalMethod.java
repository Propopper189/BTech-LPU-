// Final Method
// Note : 
// Final method cannot be overriden.

class a
{
    final void lpu()
    {
        System.out.println("Parent Method");
    }
}
class finalMethod extends a
{
    // @Override
    // void lpu() // error: lpu() in finalMethod (child) cannot override lpu() in a(parent).
    // {
        // System.out.println("Child Method");
    // }
    public static void main(String[] args) 
    {
        finalMethod obj = new finalMethod();
        obj.lpu();
    }
}