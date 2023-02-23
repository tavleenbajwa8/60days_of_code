#Code Example 1

arr = [1, 2, 0, 4, 3, 0, 5, 0]
arr_ex = []
n = len(arr)

count = 0
for i in range(n):
    if arr[i] != 0:
        arr_ex.append(arr[i])
    if arr[i] == 0:
        count = count+1

arr_f = arr_ex + [0]*count
print(arr_f)

#Code Example 2  #Time complexity (O(N**2))

arr1 = [1, 2, 0, 4, 3, 0, 5, 0]
n1 = len(arr)
count = 0

for i in range(n1):
    if arr1[i] != 0:
        arr1[count] = arr1[i]
        count += 1
        
while count < n1:
    arr1[count] = 0
    count += 1
print(arr1)


#Code Example-3 (Best) Time complexity O(N)

arr = [1, 2, 0, 4, 3, 0, 5, 0]
n = len(arr)
j = 0

for i in range(n):
    if arr[i] != 0:
        arr[j], arr[i] = arr[i], arr[j]
        j += 1
        
print(arr)

#Code Example - 4

arr = [1, 2, 0, 4, 3, 0, 5, 0]
n = len(arr)


non_zero = [i for i in arr if i != 0]
zero = [j for j in arr if j == 0]

print(non_zero + zero)
