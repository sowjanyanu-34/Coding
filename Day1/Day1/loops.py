# 1.PRINT NUMBERS FROM 1 TO N
n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    print(i)

# 2. SUM OF N NUMBERS
n=int(input("Enter the value of n:"))
s=0
for i in range(1,n+1):
    s=s+i
print ("The sum of digits is:",s)

# 3. MULTIPLICATION TABLE
n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    print(n*i)

# 4.COUNT DIGITS IN AN NUMBER
n=int(input("Enter the value of n:"))
count=0
while n>0:
    count=count+1
    n=n//10
print("The count of digits is :",count)

# 5.REVERSE A NUMBER 
n=int(input("Enter the value of n:"))
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
print("The reverse of digits is :",rev)

# 6. SUM OF DIGITS
n=int(input("Enter the value of n:"))
s=0
while n>0:
    s=s+n%10
    n=n//10
print( "Sum of given digits is:",s)

# 7.palindrome Checker
n=int(input("Enter the value of n:"))
temp=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
print("YES it is palindrome" if temp==rev else "NO it is not palindrome")

# 8.Factorial
n=int(input("Enter the value of n:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print( "Factorial of n is:",fact)

# 9.print Even numbers till n
n=int(input("Enter the value of n:"))
for i in range(2,n+1,2):
    print(i)

# 10.Check prime