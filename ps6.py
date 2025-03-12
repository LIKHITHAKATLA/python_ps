
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

