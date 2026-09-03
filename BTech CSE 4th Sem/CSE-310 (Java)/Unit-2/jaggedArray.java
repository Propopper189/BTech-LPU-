// in jagged arrays number of rows are 
// fixed but number of columns of every row can 
// be different

class jaggedArray
{
    public static void main(String args[])
    {
        int arr[][] = new int[3][];
        arr[0] = new int[2];
        arr[1] = new int[4];
        arr[2] = new int[3];
        java.util.Scanner sc = new java.util.Scanner(System.in);
        System.out.println("Enter the elements : ");
        for(int i = 0; i < arr.length; i++)
        {
            for(int j = 0; j < arr[i].length; j++)
            {
                arr[i][j] = sc.nextInt();
            }
        }
        System.out.println("Jagged Array : ");
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