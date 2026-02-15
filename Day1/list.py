# 1. READ A LIST AND PRINT
arr=list(map(int,input("Enter the list:").split()))
print("The enterd list is:",arr)

# 2.find the max element 
arr=list(map(int,input("Enter the list:").split()))
print(max(arr))

# 3.FIND MIN ELEMENT in an array
arr=list(map(int,input("Enter the list:").split()))
print(min(arr))

# 4.FIND sum ELEMENT
arr=list(map(int,input("Enter the list:").split()))
print(sum(arr))

# 5. REVERSE A LIST
arr=list(map(int,input("Enter the list:").split()))
print(arr[::-1])

# 6. Count even numbers
arr=list(map(int,input("Enter the list:").split()))
count=0
for i in arr:
    if i%2==0:
        count+=1
print("Count the even number is:",count)   

# 7.REMOVE DUPLICATES IN AN LIST
arr=list(map(int,input("Enter the list:").split()))
print("List after remove of duplications ",list(set(arr)))

#8. SEARCH ELEMENT 
arr=list(map(int,input("Enter the list:").split()))
x=int(input("Enter the element to be searched:"))
print("Found" if x in arr else "NOT FOUND")

# 9.FIND SECOND LARGEST
arr=list(map(int,input("Enter the list:").split()))
arr=list(set(arr))
arr.sort()
print("Second largest element in the list is:",arr[-2])

# 10.COUNT FREQUENCY 
arr=list(map(int,input("Enter the list:").split()))
x=int(input("Enter the element count:"))
print("Count frequency:",arr.count(x))

