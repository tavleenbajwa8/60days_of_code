#Code Example - 1

arr = [12, 35, 1, 10, 34, 1]
n = len(arr)
largest = second = -2454635434


#Finding largest number 
for i in range(n):
  largest = max(largest, arr[i])
print("Largest number is" ,largest)

#Finding second largest number 

for i in range(n):
  if arr[i] != largest:
    second = max(second, arr[i])
print("Second Largest Number is", second)


#Code Example-2 
arr = [12, 35, 1, 10, 34, 1]
print(sorted(arr)[-2])

#Code Example-3

arr = [12, 35, 1, 10, 34, 1]
n = len(arr)
first = second = -2147483648

for i in range(n):
  if arr[i] > first:
    second = first
    first = arr[i]

  elif (arr[i] > second and arr[i] != first):
    second = arr[i]
print("The second largest number is", second)

