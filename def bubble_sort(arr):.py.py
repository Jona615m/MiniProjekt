def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False 
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
         break
arr = [5,6,7,98,9,4,2,3445,675,345,1]
print("Not sorted list")
print(arr)

bubble_sort(arr)
print("Sorted list")
print(arr)




