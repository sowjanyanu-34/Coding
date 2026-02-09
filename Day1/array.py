# Array is an data structure which is a collection of elements stored contigously

# 1.Maximum element in an array
from operator import le


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
print("Minimum element in the list:",min_val)

# 3. Second largest element in an array
arr=list(map(int,input("Enter the value of list:").split()))
arr.sort()
print("Second largest element in the list:",arr[-2])

# 4. Maximum and minimum difference
arr=list(map(int,input("Enter the value of list:").split()))
max_val=min_val=arr[0]
for i in arr:
    if i>max_val:
        max_val=i
    if i>min_val:
        min_val=i
print("Maximum and minimum difference:",max_val-min_val)

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

# Access the element in an array
arr=[1,2,3,4,5,6]
for i in arr:
    print("The entered elements are:",i)

# Reverse ana rray
arr=[1,2,3,4,5]
l=0
r=len(arr)-1
while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1
print("The reversed array is:",arr)

#Most frequent Elements i na array
arr=[1,2,1,3,4,2,1,6,1]
freq={}
for x in arr:
    freq[x]=freq.get(x,0)+1
print("The frequency of element is:",freq)
max_ele=None
max_count=0
for key in freq:
    if freq[key]>max_count:
        max_count=freq[key]
        max_ele=key
print("The most frequent element in an array is:",max_ele)

# Unique elements in an array
arr=[1,2,1,3,4,2,1,6,1]
freq={}
for x in arr:
    freq[x]=freq.get(x,0)+1
print("The frequency of element is:",freq)
unique=[]
for key in freq:
    if freq[key]==1:
        unique.append(key)
print("The unique element in an array is:",unique)

#Duplicates in an array
arr=[1,2,1,3,4,2,1,6,1]
freq={}
for x in arr:
    freq[x]=freq.get(x,0)+1
print("The frequency of element is:",freq)
duplicate=[]
for key in freq:
    if freq[key]==1:
        duplicate.append(key)
print("The duplicate elements in an array is:",duplicate)

#Ananagram
s1="sowju"
s2="jowsu"
freq1={}
freq2={}
for x in s1:
    freq1[x]=freq1.get(x,0)+1 
for x in s2:
    freq2[x]=freq2.get(x,0)+1
print("The frequency of element is:",freq1)
print("The frequency of element is:",freq2) 
print(freq1==freq2)

#Frequency
arr=[1,2,1,3,4,2,1,6,1]
freq={}
for x in arr:
    freq[x]=freq.get(x,0)+1
print("The frequency of element is:",freq)

#print positive negative or zero
n=int(input("Enter a number:"))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")

#Even or Odd
n=int(input("Enter a n:"))
if n%2==0:
    print("Even")
else:
    print("Odd")

# Comapre two number
a=int(input("enter the value of a:"))
b=int(input("Enter the value of b:"))
if a>b:
    print("a is greater")
elif a<b:
    print("b is greater")
else:
    print("Equal")

#Check string is empty or not
s=int("Enter a string:")
if len(s)==0:
    print("String is empty")
else:
    print("String is not empty")

# print first charcter is vowel or constant
s=input("ENter the string:")
if len(s)==0:
    print("empty string")
else:
    ch=s.lower()
    if ch in ['a','e','i','o','u']:
        print("Vowel")
    else:
        print("constant")

#String length
s=int("Enter a string:")
if len(s)>5:
    print("greater than 5")
else:
    print("less than or equal to 5")

#Print 1 to N
n=int(input("Enter a number"))
for i in range(1,n+1):
    print(i)

#Sum of N Numbers
n=int(input("Enter the value of n:"))
i=1
total=0
while i<=n:
    total+=i
    i+=1
print("Sum=",total)

#Factorial of a number
n=int(input("Enter the value of n:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#Reverse a number
arr=[1,2,3,4,5]
l=0
r=len(arr)-1
while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1
print(arr)

#Reverse a number
n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed number =", rev)

#Count the number of digits in a number
n = int(input("Enter number: "))
count = 0
while True:
    count += 1
    n = n // 10
    if n == 0:
        break
print("Number of digits =", count)

