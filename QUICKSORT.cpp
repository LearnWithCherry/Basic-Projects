#include <iostream>
using namespace std;

int partition(int arr[], int p, int r)
{
    int pivot = arr[r];
    
    int i=p-1;
    for(int j=p; j<r; j++)
    {
        if(arr[j] < pivot)
        {
            i++;
            //swap arr[i] and arr[j]
            
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            
        }
    }
    //swap pivot element with arr[i+1]
    
    int temp = arr[i+1];
    arr[i+1] = arr[r];
    arr[r] = temp;
    
    return i+1;
}

void quicksort(int arr[], int p, int r)
{
    if(p < r)
    {
        int q = partition(arr, p, r);
        quicksort(arr, p, q-1);
        quicksort(arr, q+1, r);
    }
    
    //Print array after every iteration
    cout<<"\n";
    for(int i=0; i<7; i++)
    cout<<arr[i] <<" ";
}
int main()
{
    int arr[] = {7, 5, 3, 4, 9, 6, 2};
    quicksort(arr, 0, 6);

    return 0;
}
