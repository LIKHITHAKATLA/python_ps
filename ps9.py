def check_duplicate_digits(nums):
    result = []
    for num in nums:
        num_str = str(num)
        if len(num_str) != len(set(num_str)):
            result.append(True)
        else:
            result.append(False)
    return result

# Test the function
input_list = [202, 89, 112, 88]
output = check_duplicate_digits(input_list)
print(output)



num = [3,2,10,1,7,17,29]
maxx = float('-inf')
minn = float('inf')
for i in range(len(num)):
    if num[i] > maxx:
       maxx = num[i]
    if num[i] < minn:
        minn = num[i]

def prime(j):
    if j < 2:
        return False
    for i in range(2, int(j ** 0.5) + 1):
        if j % i == 0:
            return False
    return True

prime_number = [ j for j in range(minn, maxx+1) if prime(j) ]    
print(prime_number)



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
