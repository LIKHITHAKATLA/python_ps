# sum of non prime number

num = list(map(int, input("Enter the numbers: ").split(','))) 
non_prime =[]
for j in num:
    if j in [0 , 1]  or j < 0:
        non_prime.append(j)

    else: 
        spy = True
        for i in range(2 , j):
            if j % i == 0:
                spy = False
                non_prime.append(j)
                break
        if spy:
            continue
print(non_prime)
sum = 0
for i in non_prime:
    sum = sum + i
print(sum)


# pefect number

num = int(input("enter the number"))
perfect = 0
for i in range(1,num):
    if(num % i == 0):
        perfect = perfect + i
if( num == perfect):
    print("perfect number")
else:
    print("not a perfect number")


# LCM of 2 numbers

a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))
def LCM(a, b):
    if a > b:
        greater = a
        smallest = b   

    else:
        greater = b
        smallest = a  
    for i in range(greater, a*b+1, greater):
        if i % smallest == 0:
            return i
print("LCM of", a, "and", b, "is", LCM(a, b))

# gcd of two numbers
aa = int(input("enter 1st number"))
bb = int(input("enter 2nd number"))
def GCD(aa, bb):
    if aa > bb:
        greaterr = aa
        smallestt = bb   
    else:
        greaterr = bb
        smallestt = aa
    for i in range(smallestt,0,-1):
        if aa % i == 0 and bb % i == 0:
            return i
print("GCD of", aa, "and", bb, "is", GCD(aa, bb))
