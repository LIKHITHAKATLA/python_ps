# Print all even numbers between 1 and 50 using a while loop

for i in range(0,100):
    if i % 2 == 0:
        print(i,end=" ")

# Write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2) 

num = int(input("enter the number"))
sum=0
for i in range(0,num+1):
    sum = sum + i
print("sum of ",num,"natural numbers is",sum)

# Print all even numbers between 1 and 50 using a while loop.
i = 0
while(i < 50):
    if i % 2 == 0:
        print(i,end=" ")
    i+=1

# Write a program to display the multiplication table of a given number.

num = int(input("enter the multiplication table you want"))
for i in range(1,11):
    mul = num * i
    print(num,"*",i,"=",mul )

# Write a program to calculate the factorial of a number using a while loop.

num = int(input("enter the number"))
fact = 1
i = 1
while(i < num+1):
    fact = fact * i
    i = i + 1
print('factoria of',num ,"=",fact)

# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.

for i in range(0,100):
    if (i % 3 == 0):
        print(i,end=" ")
    elif(i % 5 == 0):
        print(i,end=" ")
