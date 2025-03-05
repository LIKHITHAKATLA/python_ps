num = list(map(int, input("Enter the numbers: ").split(','))) 
prime =[]
for j in num:
    if j in [0 , 1]  or j < 0:
        continue
    else: 
        spy = True
        for i in range(2 , j):
            if j % i == 0:
                spy = False
                break
        if spy:
            prime.append(j)
print(prime)