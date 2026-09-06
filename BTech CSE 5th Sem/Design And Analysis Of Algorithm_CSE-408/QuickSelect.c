#include <stdio.h>

int partition(int arr[], int left, int right)
{
    int pivot = arr[right];
    int i = left - 1;

    for (int j = left; j < right; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;

            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[right];
    arr[right] = temp;

    return i + 1;
}

void quickSelect(int arr[], int left, int right, int k)
{
    if (left == right)
    {
        printf("The %d-th smallest element is: %d\n", k, arr[left]);
        return;
    }

    int pivotIndex = partition(arr, left, right);

    // Number of elements from left to pivot
    int leftCount = pivotIndex - left + 1;

    if (leftCount == k)
    {
        printf("The %d-th smallest element is: %d\n", k, arr[pivotIndex]);
    }
    else if (k < leftCount)
    {
        quickSelect(arr, left, pivotIndex - 1, k);
    }
    else
    {
        quickSelect(arr, pivotIndex + 1, right, k - leftCount);
    }
}

int main()
{
    int arr[5];

    printf("Enter 5 elements:\n");

    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Enter K:\n");

    int k;
    scanf("%d", &k);

    if (k < 1 || k > 5)
    {
        printf("Invalid K. Please enter K between 1 and 5.\n");
        return 0;
    }

    quickSelect(arr, 0, 4, k);

    return 0;
}