/*
Static Method / Static Function
1. static function does not require any object for it's access.
2. It can be called by it's class name.
*/
class staticFunction1
{
    static void lpu()
    {
        System.out.println("I am inside lpu function");
    }
    public static void main(String args[])
    {
        staticFunction1.lpu();
        lpu();
    }
}