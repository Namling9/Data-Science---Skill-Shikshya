# itertools : products, permutations, combinations, accumulate, groupby, and infinite iterators


# from itertools import product,permutations,combinations

# # a = [1,2]
# # b = [3]

# # prod = product(a,b, repeat= 2)
# # print(list(prod)) #[(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)] 

# a = [1,2,3]

# perm = permutations(a)
# print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# # comb = combinations(a, r = 2)
# # print(list(comb))

# from itertools import accumulate

# a = [1,2,3,4,5]
# acc = accumulate(a)
# print("num: ",a) # num:  [1, 2, 3, 4, 5]
# print(f"accumulate num: {list(acc)}") #accumulate num: [1, 3, 6, 10, 15]

# # multiple or factorial
# import operator

# mul_accu = accumulate(a, func= operator.mul)
# print(a) # [1, 2, 3, 4, 5]
# print(list(mul_accu)) # [1, 2, 6, 24, 120]

from itertools import groupby

# def smaller_than_3 (x):
#     return x < 3

# a = [1,2,3,4]
# group_obj = groupby(a, key = smaller_than_3)

# for key, value in group_obj:
#     print(f"{key} : {list(value)}")
#     # True : [1, 2]
#     # False : [3, 4]

persons = [ {"Name": "Timitthy", "Age" : 21},{"Name": "Chris", "Age" : 25},
           {"Name": "Rohan", "Age" : 23},
             {"Name": "john", "Age" : 21} ]

group_persons = groupby(persons, lambda x: x['Age'])

for key,value in group_persons:
    print(key,list(value))