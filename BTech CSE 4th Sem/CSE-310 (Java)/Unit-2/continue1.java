class continue1
{
    public static void main(String args[])
    {
        for(int i = 1; i <= 5; i++)
        {
            System.out.println(i);
            if(i == 3)
            {
                continue;
                // this continue statement will throw me to the increment/decrement.
                // it will throw me to the next iteration.
            }
            System.out.println("LPU");
        }
    }
}