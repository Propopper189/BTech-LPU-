class array1
{
    public static void main(String args[])
    {
        /*
        How to declare one array in java
        */

        int a[] = new int[5];
        int[] b = new int[5];
        // every element inside the array is initialized to 0;
        for(int i = 0; i < 5; i++)
        {
            System.out.print(a[i] + " ");
            System.out.print(b[i] + " ");
        }
    }
}