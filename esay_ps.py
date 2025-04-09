#1} Write a program to print the sum of the digits in the number.

# num=input("enter the number")
# sum=0
# for i in num:
#     sum=sum+int(i)
# print(sum)



#2} Write a program to print reverse of the given number.  

# num=input("enter the number")
# # print(num[::-1])
# l=""
# for i in num:
#     l=i+l
# print(l)

# Write a program to print factorial of the number.

# num = int(input("enter the number"))
# fact = 1
# for i in range(1 , num+1):
#     fact = fact * i
# print('factoria of',num ,"=",fact)


# Write a program to print middle character(s) in the given string or 

# str = input("enter your value or string")
# middle = int(len(str)/2)

# if (len(str)%2 == 0):
#     print(str[middle-1],str[middle]) 
# else:
#     print(str[middle])



# Write a program to check whether the sum of digits in the number except  
# first digit and digit is equal to the sum of first digit and last digit of that  number. If both the sums are equal then print equal otherwise print not  equal 

# num = input("enter the number")
# num_to_list = list(num)
# add = int(num_to_list[0]) + int(num_to_list[-1])
# # print(add)
# middle_sum = 0
# for i in range(1,len(num_to_list)-1):
#     # print(num_to_list[i])
#     middle_sum = middle_sum + int(num_to_list[i])
# # print(middle_sum)
# if(add == middle_sum):
#     print("sum of 1st and last numbers equals to the sum of middle number")
# else:
#     print("sum of 1st and last numbers not equals to the sum of middle number")


# Write a program to check whether the digits in-between the first and last  
# digit are less than first and last digit, if yes then print true, otherwise print  false.


# num = input("enter the number")
# num_list = list(num)
# output = True
# for i in range(1,len(num_list)-1):
#     if(int(num_list[0]) < int(num_list[i]) and int(num_list[-1]) < int(num_list[i])):
#         output = False
#     else:
#         output = True
# print(output)


# Write a program to print the vowels in the given string in reverse order.

# str = input("enter the string").lower()
# li = []
# for i in str:
#     if( i in ('a','e','i','o','u') and i not in li):
#         li.append(i)
# print((li))
# for j in range(len(li)):
#     for k in range(len(li)-j-1):
#         if li[k] > li[k+1]:
#             li[k],li[k+1] = li[k+1],li[k]
# print(li)

# Write a program to print the string after removing the duplicate characters  in the string.  

# str = input("enter the string")
# d = {}
# for i in str:
#     if i  in d:
#         d[i]+=1
#     else:
#         d[i] = 1
# tar = 1
# for key,value in d.items():
#     if value == tar:
#         print(key,end="")

    
str = input("enter the value ")
