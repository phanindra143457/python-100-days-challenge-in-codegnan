# type verification:

n=10
print(type(n))

num=input()
10
print(type(num),num)

# 1.if number is zero print like "entered number is zero"

m=int(input())
if m==0:
    print("entered number is zero")
print("program is done")

# 2.check if number is zero or not:
# approach 1:

num=int(input("enter a number:"))
if num==0:
    print("number is zero")
else:
    print("number is not zero")

# approach 2:

num =int(input("enter a number:"))
if num!=0:
    print("number is not zero")
else:
    print("number is zero")

#3.check if the number is even or odd:
num=int(input("enter a number:"))
if num%2==0:
    print(num,"number is even")
else:
    print(num,"number is odd")
print("program is successfully executed")

num=int(input("enter a number:"))
n=10
if num>=0 and n%2==0:
    print(num,"number is positive even")
elif n>=0 and n%2!=0:
    print(num,"number is positive odd")
elif n<=0 and n%2==0:
    print(num,"number is negitive even")
else:
    print(num,"number is negitive odd")
    
        
