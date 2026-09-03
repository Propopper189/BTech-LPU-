class exceptionHandling1
{
    public static void main(String[] args) 
    {
        /*
            Exception Handling
            Error - Compile time problem
            Exception - Run Time Problem
                1. number divided by 0 => arithmetic exception
                2. int arr[] = {7, 5, 3, 2}; => Array index out of bounds exception
                String s = "LPU"; int a = Integer.parseInt(s); => Compiles successfully but throws NumberFormatException

            Exception are of 2 types : 
                Checked Exception => exception checked at compile time (eg : I/O Operation, SQLException, ClassNotFound, FileNotFound).
                UnChecked Exception => exception are checked at the run time (eg : ArithmeticException, ArrayIndexOutOfBounds, NumberFormatException)

            Exception and Error class are children of Throwable

            5 KeyWord to handle exception
                1. try
                2. catch
                3. throw
                4. throws
                5. finally
        */
       int a = 6;
       int b = 2;
       try
       {
            // this creates the exception
            String s = "LPU";
            int d = Integer.parseInt(s);
            int c = a/b;
            System.out.println(c);
            int arr[] = {3, 2, 7, 6};
            System.out.println(arr[4]);
       }
       catch(ArithmeticException e) // we can also write "Exception e" or "Throwable e"
       {
            // catch will give you the message why exception occurred.
            System.out.println(e);
            System.out.println(e.getMessage());
            System.out.println("Divide by 0");
       }
       catch(ArrayIndexOutOfBoundsException e) // We can write multiple catch blocks for a single try
       {
            System.out.println("Array Index Not Present");
       }
       catch(Exception e) // generalized exception should be in last
       {
            System.out.println("Exception Occurs");
       }
       finally // This will execute even if no exception occurred | This will execute even if exception occured
       {
            System.out.println("Finally Block");
       }
    }
}