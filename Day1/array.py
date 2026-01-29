# Array is an data structure which is a collection of elements stored contigously

# 1.Maximum element in an array
arr=list(map(int,input("Enter the value of list:").split()))
max_val=arr[0]
for i in arr:
    if i>max_val:
        max_val=i
print("Maximum element in the list:",max_val)

#2.Minimum element in an array
arr=list(map(int,input("Enter the value of list:").split()))
min_val=arr[0]
for i in arr:
    if i<min_val:
        min_val=i
print(min_val)

# 3. Second largest element in an array
arr=list(map(int,input("Enter the value of list:").split()))
arr.sort()
print(arr[-2])

# 4. Maximum and minimum difference
max_val=min_val=arr[0]
for i in arr:
    if i>max_val:
        max_val=i
    if i>min_val:
        min_val=i
print(max_val-min_val)

# 5. Sum of all elements in an array
arr=list(map(int,input("Enter the list:").split()))
total=0
for i in arr:
    total+=i
print("The sum of all elements in an array is:",total)

# 6. Sum of even elements in an array
arr=list(map(int,input("Enter the list:").split()))
total=0
for i in arr:
    if i%2==0:
        total+=i
print("The sum of all elements in an array is:",total)
