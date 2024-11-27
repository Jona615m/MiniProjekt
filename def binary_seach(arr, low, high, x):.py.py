def binary_search(arr, low, high, x):
 
    # Returnere index af x i arr hvis den er tilstede , else -1

    #Her checker den basis kravene
    # at higher er større end lower og hvordan midten
    if high >= low:
 
        mid = (high + low) // 2
 
       
        if arr[mid] == x:
            return mid
 
        #elif (else if statement phyton sprog)
        #Hvis elementet er mindre end mid, så kan den kun fremstå i venstre subarray

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        #else statement bliver lavet og der er kun mmulighed for at elemtnetet bliver vist i højre side af subarrayet 
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
       #hvis elementet slet ikke er tilgængeligt i arrayet
        return -1
 
# Test array
arr = [ 4, 69, 377, 124, 40 ]
x = 377
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")