class twoDimArray
{
    public static void main(String args[])
    {
        int arr[][] = new int[3][2];
        System.out.println(arr.length); // prints the number of rows
        System.out.println(arr[0].length); // 1st row how many colums
        java.util.Scanner sc = new java.util.Scanner(System.in);
        for(int i = 0; i < arr.length; i++)
        {
            for(int j = 0; j < arr[i].length; j++)
            {
                arr[i][j] = sc.nextInt();
            }
        }
        System.out.println("Printing Matrix Elements : ");
        for(int i = 0; i < arr.length; i++)
        {
            for(int j = 0; j < arr[i].length; j++)
            {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}