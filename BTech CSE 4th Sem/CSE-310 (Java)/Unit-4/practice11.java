class outer
{
    static int x = 5; // if its not static variable it cannot be accessed by the static inner class
    static class inner
    {
        void lpu()
        {
            System.out.println("LPU");
            System.out.println(x);
        }
    }
}
class practice11
{
    public static void main(String[] args) 
    {
        outer.inner obj = new outer.inner();
        obj.lpu();    
    }
}