// sum of longest sub sequence of even numbers in an array
// find the sum of longest subsequence in an arry
// if more than one longest subsequence comes, result will be addition of those
class importantExam
{
    public static void main(String[] args) 
    {   
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i = 0; i < n; i++)
        {
            arr[i] = sc.nextInt();
        }
        int currLen = 0;
        int currSum = 0;
        int maxLen = 0;
        int maxSum = 0;

        for(int i = 0; i < n; i++)
        {
            if(arr[i] % 2 == 0)
            {
                currLen++;
                currSum = currSum + arr[i];
            }
            else
            {
                if(currLen > maxLen)
                {
                    maxLen = currLen;
                    maxSum = currSum;
                }
                else if((currLen == maxLen) && maxLen > 0)
                {
                    maxSum = maxSum + currSum;
                }
                currSum = 0;
                currLen = 0;
            }
        }
        if(maxSum == 0)
        {
            System.out.println(-1);
            System.exit(0);
        }
        else if(maxLen < currLen)
        {
            System.out.println(currSum);
            return;
        }
        System.out.println(maxSum);
    }
}