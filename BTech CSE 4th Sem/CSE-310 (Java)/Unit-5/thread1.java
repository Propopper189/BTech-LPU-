// Create a thread by extending to thread class

class A extends Thread
{
    public void run()
    {
        System.out.println("Thread Created!");
    }
}
class thread1
{
    public static void main(String args[])
    {
        A obj = new A();
        obj.start(); // automatically the run method will be called.

    }
}