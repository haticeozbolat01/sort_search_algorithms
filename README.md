# sort_search_algorithms

## Sorting Algorithms in Python

Sorting is defined as an arrangement of data in a certain order. Sorting techniques are used to arrange data(mostly numerical) in an *ascending* or *descending order*.


![image](https://user-images.githubusercontent.com/74445249/225334869-8618cc5b-8697-41f1-9bf7-3f6fe3360dd2.png)

Some of the real-life examples of sorting are : Telephone Directory, Dictionary, Contact List

### Bubble Sort

https://user-images.githubusercontent.com/74445249/225340119-8e31945c-9a00-4b1e-bfc9-0f73d446f47c.mp4



* Time Complexity: O(n^2)

* Auxiliary Space: O(1)

### Selection Sort

![selectionsortdemo](https://user-images.githubusercontent.com/74445249/225342551-33f91ae9-e1f3-41b8-975f-9b256f8aa776.gif)



* Time Complexity: O(n^2)


* Auxiliary Space: O(1)

### Insertion Sort

![Insertion-sort-example](https://user-images.githubusercontent.com/74445249/225343174-04ec03ed-39ba-483e-8991-1c416a7fb0fc.gif)


* Time Complexity: O(n^2)

* Auxiliary Space: O(1)


## Searching Algorithms in Python 

Searching Algorithms are designed to check for an element or retrieve an element from any data structure where it is stored.

### Linear Search 


![linear_search](https://user-images.githubusercontent.com/74445249/225344591-7d5d5029-137c-4590-bb83-a435ef8c4d07.gif)



Step 1: First, read the search element (Target element) in the array.

Step 2: In the second step compare the search element with the first element in the array.

Step 3: If both are matched, display “Target element is found” and terminate the Linear Search 
function.

Step 4: If both are not matched, compare the search element with the next element in the array.

Step 5: In this step, repeat steps 3 and 4 until the search (Target) element is compared with the 
last element of the array.

Step 6 – If the last element in the list does not match, the Linear Search Function will be 
terminated, and the message “Element is not found” will be displayed


* Time complexity: O(N)

* Auxiliary Space: O(1)


### Exponential Search

 
The idea is to start with subarray size 1, compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater. 


![animation-541x141](https://user-images.githubusercontent.com/74445249/225350759-5b693f53-45ef-4485-9993-d38e0e6c3433.gif)


Exponential search involves two steps:  

1. Find range where element is present

2. Do Binary Search in above found range.

* Time Complexity : O(Log n) 

* Auxiliary Space :  O(1) space.






