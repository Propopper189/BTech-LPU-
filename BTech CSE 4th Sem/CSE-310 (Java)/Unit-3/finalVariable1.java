class finalVariable1
{
    final int a = 5; // possible 

    // This is also possible : 
    // final int a;
    // finalVariable1()  // Constructor
    // {
    //     a = 5;
    // }

    // once initialized, it cannot be changed;
    // final variable must be initialized directly or only inside constructor.
    void display()
    {
        // a = 5; // cannot initialize in function
        System.out.println(a);
    }
    public static void main(String args[])
    {
        new finalVariable1().display();
    }
}