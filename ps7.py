#sum of nested lists into list
# input [1,2,3,[5,6,7,1],[1,2,3],[1,4,3]]
# output : [19, 6, 8]
# list1 = [1,2,3,[5,6,7,1],[1,2,3],[1,4,3]]
# list = []
# for i in list1:
#     if isinstance(i, list):
#         sum = 0
#         for j in i:
#             sum = sum + j
#         list.append(sum)
# print(list)

# max and min value in nested list

list1 = [1,2,3,[5,6,7,14],[9,2,3],[1,4,3,10]]
sum_list = []
max_value = float('-inf')
min_value = float('inf')
for i in list1:
    if isinstance(i, list):
        sum = 0
        for j in i:
            sum = sum + j
        sum_list.append(sum)
        for j in i:
            if j > max_value:
                max_value = j
            if j < min_value:
                min_value = j
print("Maximum value =",max_value)
print("Minimum value =",min_value)
print("Sum of nested lists",sum_list)




