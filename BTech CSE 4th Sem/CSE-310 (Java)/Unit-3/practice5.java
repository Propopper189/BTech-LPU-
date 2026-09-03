// Write a program to accept an array and find a pair of elements whose sum is equal to target
class practice5
{
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i = 0; i < n; i++)
        {
            arr[i] = sc.nextInt();
        }
        int l = 0;
        int r = arr.length-1;
        int t = sc.nextInt();
        java.util.Arrays.sort(arr);
        // Continue
    }
}