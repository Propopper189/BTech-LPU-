public class practice5 {
    public static void main(String args[])
    {
        // 2D array
        int arr[][] = new int[10][10];
        int k = 1;
        for(int i = 0; i < 10; i++)
        {
            for(int j = 0; j < 10; j++)
            {
                arr[i][j] = k++;
            }
        }
        for(int i = 0; i < 10; i++)
        {
            for(int j = 0; j < 10; j++)
            {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

        // Jagged Array
        k = 1;
        int arr2[][] = new int[10][];
        for(int i = 0; i < arr2.length; i++)
        {
            arr2[i] = new int[10];
            for(int j = 0; j < arr2.length; j++)
            {
                arr2[i][j] = k++;
            }
        }
        System.out.println("\nPrinting jagged array : ");
        for(int i = 0; i < arr2.length; i++)
        {
            for(int j = 0; j < arr2.length; j++)
            {
                System.out.print(arr2[i][j] + " ");
            }
            System.out.println();
        }
        System.exit(0);
    }
}
