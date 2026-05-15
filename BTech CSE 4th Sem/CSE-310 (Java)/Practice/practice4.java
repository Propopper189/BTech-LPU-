public class practice4 {
    public static void main(String args[])
    {
        int n = 10;
        for(int i = 1; i <= n; i++)
        {
            System.out.println(i + " ");
        }
        for(int i = 11; i <= 20;)
        {
            System.out.println(i++ + " ");
        }
        int i = 21;
        for(; i <= 30;)
        {
            System.out.println(i++ + " ");
        }
        for(;;)
        {
            int j = 1;
            System.out.println("Ran Infinite");
            j += 1;
            if(j == 2)
            {
                break;
            }
        }
        int arr[] = {1, 3, 4};
        for(int k : arr)
        {
            System.out.print(k + " ");
        }
    }
}
