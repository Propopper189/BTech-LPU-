// Create a thread by implementing to runnable interface
class A implements Runnable
{
    // Best when overriding only run method, because we can extend to more class
    public void run()
    {
        System.out.println("Thread Created");
    }
}
public class thread2 {
    public static void main(String args[])
    {
        Thread obj = new Thread(new A());
        obj.start();
    }
}
