# check the input is(-ve or +ve)even or (-ve or +ve)odd
n=int(input())

if n%2==0:
    if n>-1:
        print("number is +ve even")
    else:
         print("number is -ve even")
else:
    if n>-1:
        print("number is +ve even")
    else:
        print("number is -ve odd")


#loops
#check which one even number or odd number in the given list of number

lst=[2,4,3,5,6,9,4]

for num in lst:
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
print("program done")

#check which one +ve number or -ve number in the given list of number

lst=[2,4,-3,5,-6,-7,9]

for num in lst:
    if num>=0:
        print(num,"is positive")
    else:
        print(num,"is negitive")
print("program done")

#print 1-40 numbers using range function

for s in range(40):
    print(s)

#print even numbers 0 to 50:

for num in range(0,50,2):
    print(num)
