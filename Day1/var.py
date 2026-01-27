# INPUT HANDLING
n = int(input("Enter the value of n: "))
print("This is the entered value:",n)

# ADD TWO NUMBER
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
sum=a+b
print("The sum is ",sum)

#CHECK ODD OR EVEN 
n=int(input("Enter a value n:"))
if n%2==0:
    print("n is even")
else:
    print("n is odd")    

#CHECK POSITIVE NEGATIVE ZERO
n=int(input("Enter n:"))
if n>0:
    print("N is positive")
elif n<0:
    print("N is negative")
else:
    print("N is Zero")

#FIND SQUARE AND CUBE
n=int(input("Enter the value of n:"))
print("The sqaure of the n is",n*n)
print("The sqaure of the n is",n*n*n)

#SWAP 2 NUBERS
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
a,b=b,a
print("The swapping number is",a,b)

#AREA OF CIRCLE
r=float(input("Enter the radius:"))
area=3.14*r*r
print("The area of circle is:",area)

#CHECK DIVISIBLE BY 5
n=int(input("Enter the value of n:"))
if n%5==0:
    print("Divisible by 5")
else:
    print("It is not divisible by 5")

#MAX OF 2 NUMBERS
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
if a>b:
    print(a,"is greater")
else:
    print(b,"is greater")
    
#COVERT CELSIUS TO FAHRENHEIT
c=float(input("Enter the celsius value:"))
f=(c*9/5)+32
print("The corresponding fahrenheit value is",f)