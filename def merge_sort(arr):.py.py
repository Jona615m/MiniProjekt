def merge_sort(arr):
    #Vi laver dette da arrayret er soretd hvis den er på 1
    if len(arr) > 1:
        #len = length
        #I python er der en nutation der gør at :" opdeler det
        #Fra 0 til midten af arr da vi siger den skal dele med 2
        left_arr = arr[:len(arr)//2]
        #Her gør vi det fra den modsatte side, så her tager den fra midten til slutningen
        right_arr = arr[len(arr)//2:]
        
        #Recursion
        merge_sort(left_arr)
        merge_sort(right_arr) 

        #Merge

        l = 0
        r = 0
        #index der holder styr på merge
        m = 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                arr[m] = left_arr[l]
                l += 1
                m += 1
                
            else:
                arr[m] = right_arr[r]
                r += 1
                m += 1
        
        while l < len(left_arr):
            arr[m] = left_arr[l]
            l += 1
            m += 1
        
        while r < len(right_arr):
            arr[m] = right_arr [r]
            r += 1
            m += 1
        

arr = [38,27,43,3,9,82,10]
print("Not sorted list")
print(arr)

merge_sort(arr)
print("sorted list")
print(arr)