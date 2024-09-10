# Question : Variable-length Arguments (*args and **kwargs)
# Write a Program to Define a Function `describe_pet` that accepts a variable number of keyword arguments (`**kwargs`).
 
# The function should print the details of these keyword arguments as "property: value". Call this function with pet details like name, age, and type
# Python
# Input :  describe_pet(name="Rex", age=5, type="dog")
# Output : name: Rex
#          age: 5
#          type: dog

# def descrip_pet(**kwargs):
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
    

# descrip_pet(name = "Rex", age = 5, type = "dog")

'''
output: 

{'name': 'Rex', 'age': 5, 'type': 'dog'}
name: Rex
age: 5
type: dog

'''


from math import sqrt
# Question : Calculate Std. Deviation of given list.

def standardDeviation(list1):
    n = len(list1)
    mean = sum(list1) / n
    list2 = [(x-mean)**2 for x in list1]
    sd = sqrt(sum(list2)/n)
    return f"Standard Deviation of your list : {sd:.3f}"
    
l1 = [2,5,34,12,31,424,532,5,67,44,90,54]

print(standardDeviation(l1)) #Standard Deviation of your list : 168.751
    

