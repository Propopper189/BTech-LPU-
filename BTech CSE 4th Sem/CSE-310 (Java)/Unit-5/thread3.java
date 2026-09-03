// Write a program to print from 1 to 10, use sleep() method
class A extends Thread
{
    public void run()
    {
        try
        {
            for(int i = 1; i <= 10; i++)
            {
                System.out.print(i + " ");
                Thread.sleep(1000); // 1000ms = 1 second
            }
        }
        catch(Exception e){}
    }
}
public class thread3 {
    public static void main(String args[])
    {
        A obj = new A();
        obj.start();
    }
}
