#printing single number
print(2)    #1
  
#printing multiple numbers
print(2,5)    #2,5

# arthemetic operations without using variables 
print(5+7)        #12
print(9-4)        #5
print(7*7)        #49
print(6/5)        #1.2
print(4**3)       #64

# arthemetic operations using variable

num1 =45
num2 = 23
print( num1 + num2 )   #68
print( num1 - num2 )   #-22
print( num1 * num2 )   #1035
print( num1 / num2 )   #1.9565217391304348
print( num1 // num2 )  # 1

# strings

print("hii")      #hii
str1= "hii frineds" 
print(str1)         #hii frineds
print(type(str1))  #<class 'str'>
print(len(str1))     #11 

# reassinging to the varibale
str1 = "how are you"
print(str1)     #how are you
print(len(str1))     #11

# indexing
# print char Index value consisting 5 
print("indexing")
print(str1[2])   #w
print(str1[-1])    #u

#slicing
#It is denoted by colon(:) is used to prints the sub string

print("Slicing") 
print(str1[0:3]) #how
print(str1[4:6])# ar
print(str1[4:])# are you
print(str1[:7])  #how are
print(str1[:]) #how are you
print(str1[8:20]) #you

print("After Reverse Slicing")
print(str1[-10:-3]) #ow are

print(str1[-2:-9 : -1]) #oy era
print(str1[0 : : 2]) #hwaeyu
print(str1[-2: :-2])  #o r o
# ARTHEMATIC OPERATORS
print("ARTHEMATIC OPERATORS")
a = 2
b = 3
print(a +  b)       # 5
print(a - b)        # -1
print(a * b)        # 6
print(a / b)        # 0.66666
print(a % b)        # 2
print(a // b)       # 0
print(a ** b)       # 8

a= 5 + 3j
b= 6-5j
print(a + b )
print(a - b )
print(a * b )
print(a ** b )
print(a / b )
# print(a // b )
# print(a % b )

list1 = [1,2,3,4,5,[6,7,8,9],"LIKHITHA"]
print(list1)
print(type(list1))
print(list1[5])     #[6,7,8,9]
print(list1[-1])     #LIKHITHA
print(list1[-1][-1])   #A

list1[1]="hii"
print(list1)     #[1, 'hii', 3, 4, 5, [6, 7, 8, 9], 'LIKHITHA']

list1=[2,5,3,"no"]
print(list1)    #[2, 5, 3, 'no']
print(list1[1:4])  #[5,3,"no"]
print(list1[4:1])  #[]
print(list1[4:1:-1])  #['no', 3]


tup=(1,2,4,5,"no",[5,6,7])
print(tup)    #(1, 2, 4, 5, 'no', [5, 6, 7])
print(tup[1:4])   #(2, 4, 5)
print(tup[4:1])  #[]
print(tup[4:1:-1])   #('no', 5, 4)
# tup[1]="yes"
# print(tup)  #tuple' object does not support item assignment



def multiple(num1):
    return num1 % 3 == 0
   
print(multiple(6))
print(multiple(7))

def multiple(num1):
    if(num1 % 3 == 0 and num1 % 5 == 0):
        return "FizzBuzz"
    elif(num1 % 3 == 0):
        return "Fizz"
    elif(num1 % 5 == 0):
        return "Buzz"
    else:
        return num1
print(multiple(3))
print(multiple(10))
print(multiple(15))
print(multiple(7))

def sum(num1,num2):
    return num1 + num2
def sum(num1,num2,num3):
    return num1 + num2 + num3
def sum(num1,num2,num3,num4):
    return num1 + num2 + num3 + num4

print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,3,4))


def fun(a,*args):
    sum=a
    for i in args:
        sum = sum * i
    return sum
print(fun(1,2,3))
print(fun(1,2,3,4))


print(list(map(lambda x:x +5,[1,2,3,4,5,6])))

print(list(filter(lambda x:x +5,[1,2,3,4,5,6])))

y = list(filter(lambda x:x % 2 == 0,[1,2,3,4,5,6]))
print(list(map(lambda x:x **2,y)))




print(list(filter(lambda x : len(x) > 5, ["hi","how are you","not bad"])))

# ASSIGNMENT OPERATOR
print("ASSIGNMENT OPERATOR")
a,b = 2,7
a+=b
print(a)  #9

a,b = 2,7
a-=b
print(a)   #-5

a,b = 2,7
a*=b
print(a)   #14

a,b = 2,7
a/=b
print(a)   #0.2857142857142857

a,b = 2,7
a%=b
print(a)  #2

a,b = 2,7
a//=b
print(a)   #0

a,b = 2,7
a**=b
print(a)   #128

print("LOGICAL OPERATOR")
#LOGICAL OPERATOR
print("AND")
print(2 and 3)           #3
print(3 and 2)           #2
print(3 > 2 and 2 < 1)   # False
print(3 > 2 and 6 > 5 and 2 < 8)    # True


print("or")
print(2 or 3)            #2
print(3 or 1)            #3
print(2 < 3 or 5 < 6)   #True

print("not")
a = False
print(not a)             #True


print("RELATIONAL OPERATORS")
a = 10
b = 13
c = 13
print(a >  b)       # False
print(a < b)        # True
print(a >= c)        # False
print(a <= c)        # True

print("BITWISE OPERATOR")
a = 2
b = 5
print(a &  b)       # 0
print(a | b)        # 7
print(a ^ b)        # 7
print( ~a )         # -3
print(a << 2)       # 8
print(b >> 2)       # 1

