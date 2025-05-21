'''
Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Input: arr[] = [1, 3 , 2]
Output: [1, 2, 3]

Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105


def merge(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge(arr, low, mid)
    merge(arr, mid + 1, high)
    Sort(arr, low, mid, high)
def Sort(arr, low, mid, high):
    i = low
    j = mid + 1
    k = []
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            k.append(arr[i])
            i += 1
        else:
            k.append(arr[j])
            j += 1
    while i <= mid:
        k.append(arr[i])
        i += 1
    while j <= high:
        k.append(arr[j])
        j += 1
    for ind, val in enumerate(k):
        arr[low + ind] = val
arr=list(map(int,input().split()))
merge(arr,0,len(arr)-1)
print(arr) '''