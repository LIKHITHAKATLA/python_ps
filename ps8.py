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



