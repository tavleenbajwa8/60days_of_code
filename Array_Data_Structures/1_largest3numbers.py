# Find the largest three distinct elements in an array

#Code Example-1
import sys
 
def largest_3(arr,n):
  if n < 3:
    print("Invalid Input")

  third = first = second = -sys.maxsize

  for i in range(0, n):
    if arr[i] > first:
      third = second 
      second = first 
      first = arr[i]

    elif arr[i] > second:
      third = second
      second = arr[i]

    elif arr[i] > third:
      third = arr[i]
  print("Three largest elements are: ", first, second, third)


arr = [2,6,5,3,1,9,7,11]
n = len(arr)

largest_3(arr, n)


#Code Example 2

arr = [40,6,50,3,1,90,7,11]
n = len(arr)

sorted_list = sorted(arr)
print(sorted_list[-1:-4:-1])

#Code Example 3
