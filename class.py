
# write a program to check if three sides length form a valid triangle. 

# a = int(input("enter the a side vaule"))
# b = int(input("enter the b side vaule"))
# c = int(input("enter the c side vaule"))
# if ((a + b > c) and (a + c > b) and (b + c > a) ):
#     print("valid triangle")
# else:
#     print("not a valid triangle")


# Write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2) 

# num = int(input("enter the number"))
# sum=0
# for i in range(0,num+1):
#     sum = sum + i
# print("sum of ",num,"natural numbers is",sum)

# Write a program to display the multiplication table of a given number.

# num = int(input("enter the multiplication table you want"))
# for i in range(1,11):
#     mul = num * i
#     print(num,"*",i,"=",mul )


# write a program to count the number of digits in a given number using a  while  loop. 

# num = input("enter the number")
# count = 0
# i = 0
# while(i < len(num)):
#     count = count + 1
#     i = i + 1
# print(count)

# Reverse a number using a  while  loop. 

# num = input("enter the number")
# reverse = ""
# sum = 0
# i = 0
# while(i < len(num)):
#     reverse = num[i] + reverse
#     sum = sum + int(num[i])
#     i = i + 1
# print(reverse)
# print(sum)


# Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a  while  loop. 
# a=1
# while(1):
#     if ( a >= 0):
#         a = int(input("enter the number"))
#     else:
#         print("you entered a negative number")

 
# Print reverse of a number

# num1 = 12345
# sum = 0
# rev = 0
# while num1 > 0:
#     rem = num1 % 10
#     sum = sum + rem
#     num1 = num1 // 10
#     rev = rev * 10 + rem
# print(sum)
# print(rev)

 
# Print the first 10 terms of the Fibonacci series using a  for loop.
# n = int(input("enter the number"))
# f0 = 0
# f1 = 1
# f2 = 2
# print(f0,end=" ")
# print(f1,end=" ")
# print(f2,end=" ")
# for i in range(0,n):
#     f0 = f1
#     f1 = f2
#     f2 = f0 +f1
#     print(f2, end=" ")

#check the input prime or not
#approch 1
# num = int(input("enter the value"))
# spy = False
# if num in [0 , 1] or num < 0:
#     print("not a prime number")
# else: 
#     for i in range(2 , num):
#         if num % i == 0:
#             spy = True
#             print("not a prime")
#             break
#     if spy == False:
#         print("prime")

# 9- 1,3,9======9//2=4
# half next no divisors after 14 not divisors upto 28
# 28- 1,2,4,7,14,28======28//2=14

# num = int(input("enter the value"))
# spy = False
# if num in [0 , 1] or num < 0:
#     print("not a prime number")
# else: 
#     for i in range(2 , (num // 2) + 1):      
#         if num % i == 0:
#             spy = True
#             print("not a prime")
#             break
#     if spy == False:
#         print("prime")


# num = int(input("enter the value"))
# spy = False
# if num in [0 , 1] or num < 0:
#     print("not a prime number")
# else: 
#     for i in range(2 , int(num ** 0.5) + 1):
#         if num % i == 0:
#             spy = True
#             print("not a prime")
#             break
#     if spy == False:
#         print("prime")

# implement a menu-driven program where the user can choose to: 

# 1.  Find the square of a number. 
# 2.  Find the cube of a number. 
# 3.  Exit.
# num = int(input("enter the number"))
# square = []
# cube = []
# for i in range(0,num):
#     square.append(i*i)
#     cube.append(i*i*i)
# print(square)
# print(cube)


# spy = True
# while(spy):
# while(True):
#     num = input("enter the  1.square , 2.cube , 3.exit").lower()
#     if num == "square":
#         squ = int(input("enter the number")) 
#         print("square of",squ,"=",squ*squ)
#     elif num == "cube":
#         squ = int(input("enter the number")) 
#         print("square of",squ,"=",squ*squ*squ)
#     elif num == "exit":
#         print("you are existed")
#         # spy = False
#         break
#     else:
#         print("enter the valid one")


# implement a basic login system where the user has three attempts to enter the correct password using a loop.
# 
# user = input("enter the user name")
# password = input("enter the password")
# for i in range(3,0,-1):
#     c_user = input("enter the user name")
#     c_password = input("enter the password again")
#     if password != c_password and c_user != user:
#         print(f"you have {i-1} chance")
#     else:
#         print("login suscessful")

# POLINDROME

# original =  int(input("enter the number"))
# num = original
# rev = 0
# while num > 0 :
#     rem = num % 10
#     num = num // 10
#     rev = rev * 10 + rem
# print(rev)
# if original == rev:
#     print("p")
# else:
#     print("not")
    
# ------------------------nearest prime---------------------------------------------------

# num = int(input("enter the number"))
# lefttemp = num
# righttemp = num
# right_side_prime = -1
# left_side_prime = -1
# def check_prime(input_num):
#     if input_num in [0,1]:
#         return False
#     for i in range(2,input_num):
#         if input_num % i == 0:
#             return False
#     return True
# while True:
#     lefttemp-=1
#     if(lefttemp <= 1):
#         break
#     if check_prime(lefttemp):
#         left_side_prime = lefttemp
#         break
# print(left_side_prime)
# while True:
#     righttemp+=1
#     if check_prime(righttemp):
#         right_side_prime = righttemp
#         break
# print(right_side_prime)
# left_distance = num - left_side_prime
# right_distance = right_side_prime - num
# if left_side_prime == -1:
#     print(right_side_prime)
# elif(left_distance == right_distance):
#     print(left_side_prime,right_side_prime)
# elif left_distance < right_distance:
#     print("near prime",left_side_prime)
# elif(left_distance > right_distance):
#     print(right_side_prime)

# list = [3,2,5,2,8]
# max = float('-inf')
# sum = 0
# min = float('inf')
# for i in range(len(list)):
#     sum = sum + list[i]
#     if list[i] > max:
#        max = list[i]
#     if list[i] < min:
#         min = list[i]
# print(max)
# print(min)
# print(sum)

# def fun(list):
#     maxx = 0
#     sum = 0
#     minn = 10
#     for i in range(len(list)):
#         sum = sum + list[i]
#         if list[i] > maxx:
#             max = list[i]
#         if list[i] < minn:
#             min = list[i]
#     print(maxx)
#     print(minn)
#     print(sum)
# fun([3,2,5,2,8])

# list = [1,2,5,4,6]
# low = 0
# hegh = len(list)-1
# while(low < hegh):
#     list[low] , list[hegh] = list[hegh] , list[low]
#     low = low + 1
#     hegh = hegh - 1
# print(list)




# list = [1,4,6,"ture"]
# rev_list = []
# for i in range(len(list)-1,-1,-1):
#     rev_list.append(list[i])
# print(rev_list)

# list = [1,4,6,"ture"]
# rev_list = []
# for i in list:
#     rev_list.insert(0,i)
# print(rev_list)

# list = [1,2,3,4,'ture']
# rev_list = []
# half = len(list)//2
# for i in range(half):
#     rev_list.append(list[i])

# for j in range(len(list)-1 , half-1 , -1):
#     rev_list.append(list[j])

# print(rev_list)


    

# list = [1,2,3,4,5,6,7,8]
# mid = len(list)//2
# low = mid
# hegh = len(list)-1
# while(low < hegh):
#     list[low] , list[hegh] = list[hegh] , list[low]
#     low = low + 1
#     hegh = hegh - 1
# print(list)

# passs = input("enter ths password")
# list = ['#','@','$','&','*']
# for i in range(65,91):
#     list.append(chr(i))
# for i in range(97,123):
#     list.append(chr(i))
# for i in range(10):
#     list.append(i)
# # print(list)
# count = 0
# for i in passs:
#     if i in list:
#         count = count + 1
#         break
# print(count)


# cap = 0
# small = 0
# specail = 0
# num = 0
# for i in passs:
#     if 'A' <= i <= 'Z':
#         cap = cap + 1
#     elif 'a' <= i <= 'z':
#         small = small + 1
#     elif(i in list):
#         specail = specail + 1
#     elif 0 <= int(i) <= 9:
#         num = num + 1
# if(cap >= 1 and small >= 1 and specail >= 1 and num >= 1 and len(passs) > 7):
#     print("strong password")
# elif( small >= 1 and specail >= 1 and num >= 1):
#     print("medium")
# else:
#     print("weak")



# --------------------------sum of numbers of each index in the list ------------------
# list = [202 , 89 , 112 , 88]
# sum_list = []
# for num1 in list:
#     sum = 0
#     while num1 > 0:
#         rem = num1 % 10
#         # sum = sum + rem
#         num1 = num1 // 10
#         if rem % 2 == 0:
#             sum = sum + rem
#     sum_list.append(sum)
# print(sum_list)


# list1 = [1,3,4,10,5,2]
# list2 = [2,4,3,1,7,5,15]
# flag = True
# for i in list1:
#     if i in list2:
#         flag = True
#         # continue
#     else:
#         flag = False
#         break
# if(flag):
#     print("substring")
# else:
#     print("not a substring")

#second higest number in the given list#############

# l=[1,4,2,6]
# max=1
# secmax=-1
# for i in range(len(l)):
#     if(max<l[i]):
#         max=l[i]
# print(max)
# for i in range(len(l)):
#     if (secmax<l[i] and max>l[i]):
#         secmax=l[i]
# print(secmax)

# l = [20,15,26,2,98,6]  #4 3 5 1 6 2
# output = []
# l2 = sorted(l)         #[2, 6, 15, 20, 26, 98]
# print(l2)
# for i in range(len(l)):
#     for j in range(len(l2)):
#         if(l2[j] == l[i]):
#             output.append(j+1)
#             break
# print(output)


# def power(input_num,powr):
#     if(powr == 0):
#         return 1
#     return input_num * power(input_num,powr-1)
# print(power(5,2))

# def fibbi(n):
#     if n <= 1:
#         return 1
#     return fibbi(n-1) + fibbi(n-2)
# print(fibbi(6))

# def revers(input_str):
#     if len(input_str)<=1:
#         return input_str
#     return input_str[-1] + revers(input_str[0 : len(input_str)-1])
# print(revers("hello"))

# def listrevrse(input_list):
#     if len(input_list) <=1:
#         return input_list
#     newlist = []
#     return [input_list[-1]] + listrevrse(input_list[0:len(input_list)-1])
# list1 = [2,4,5,6]
# print(listrevrse(list1))