# Let's do a coding that we will write sorting and search algorithms into functions.

# Sorting algorithms: Bubble Sort, Selection Sort, Insertion Sort
# Search algorithms : Linear Search, Exponential Search


# Bubble Sort : Time Complexity: O(n2), Auxiliary Space: O(1)
def bubble_sort(arr):
  n= len(arr) # Assing to n array length

  for i in range(n): # for loop to traverse through all
      for j in range(0, n-i-1):  # Range of the array is from 0 to n-i-1
        if arr[j] > arr[j+1]:  # Swap the elements if the element found
           arr[j], arr[j+1] = arr[j+1], arr[j]   #is greater than the adjacent element

  print(arr)

# Selection Sort: Time Complexity: O(n2), Auxiliary Space: O(1)
def selection_Sort(array):
    size = len(array)
    for s in range(size):
        min_idx = s
        for i in range(s+1, size):  # For sorting in descending order
            if array[i] < array[min_idx]: # for minimum element in each loop
               min_idx = i

        (array[s],array[min_idx]) = (array[min_idx],array[s]) # Arranging min at the correct position

    print(array)

# Insertion Sort: Time Complexity: O(n2) ,  Auxiliary Space: O(1)
def insertion_sort(array):
    # Loop from the second element of the array until the last element
    for i in range(1,len(array)):
        key_item = array[i] # This is the element we want to position in its correct place
        j = i-1  # Initialize the variable that will be used to find the correct position of the element reference
        # by `key_item`
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
              array[j+1] = array[j]
              j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location

        array[j+1] = key_item

    print(array)

# Linear Search Algorithm: Time complexity: O(N), Auxiliary Space: O(1)

def linear_search(arr,element):

    for i in range(len(arr)):
        if arr[i] == element: # If x is present then return its location
           return i
    return -1


# Exponential Search: Time Complexity : O(Log n) , Auxiliary Space :  O(1) space.

def exponential_search(arr,x):
    n = len(arr)
    if n == 0:
       return-1
    i = 1
    while i < n and arr[i] < x:
         i *= 2

    left = i // 2
    right = min(i,n-1)

    while left <= right:
        mid = ( left + right) // 2
        if arr[mid] == x:
           return mid
        elif arr[mid] < x :
             left = mid +1
        else:
            right = mid -1


    return -1

# If x is present then return its location




# Driver Code
data = [2, 3, 4, 10, 40]
data1 = [5,8,199,78,36,1,3]


bubble_sort(data1)
selection_Sort(data1)
insertion_sort(data1)
print(linear_search(data,5))
print(exponential_search(data,14))
