#------------------------------------------Function-----------------------------------------------#


# Create a function in Python...


# def panda(name,years):
#     print(name,years)

# panda("bgmi",4)



# Create a function with variable length of arguments...


# def func1(*args):
#     for i in args:
#         print(i)

# func1(20, 40, 60)
# func1(80, 100)




# Write a program to create function calculation() such that it can accept two variables and calculate 
# addition and subtraction. Also, it must return both addition and subtraction in a single return call


# def calculation(a,b):
#     addition = a+b
#     subtraction = a-b

#     return addition, subtraction

# res = calculation(90,70)

# print(res)



# def calc(a,b):
#     return a+b, a-b

# add, sub = calc(90,70)
# print(add, sub)


# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary




# def show_employee(name,salary=90000):
#     print("Name:",name, "Salary:",salary)


# show_employee("Panda",1230000000)
# show_employee("Bang")



# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it



# def outr_func(a,b):

#     def addition(a,b):
#         return a+b

#     add = addition(a,b)

#     return add+5

# result = outr_func(5,10)

# print(result)



#wap to find max of three numbers by function


# def max_of_two(x,y):
#     if x>y:
#         return x

#     return y

# def max_of_three(x,y,z):
#     return max_of_two(x, max_of_two(y,z))

# print(max_of_three(3,-6,9))




#Write a Python function to sum all the numbers in a list

# def sum(numbers):
#     t= 1
    

#     for i in numbers:

#         t*=i

#     return t

# print(sum((3,6,9,21)))



#Write a Python program to reverse a string.


# def string_reverse(str1):

#     rstr1 = ''
#     index = len(str1)

#     while index > 0:
#         rstr1 += str1[ index-1]
#         index = index-1

#     return rstr1
# print(string_reverse('pandaop'))




#Write a Python function to calculate the factorial of a number (a non-negative integer). 
#The function accepts the number as an argument.


# from math import factorial


# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fac(n-1)

# n = int(input("Input a number to compute factorial : "))
# print(factorial(n))





#Write a Python function to check whether a number falls in a given range


# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(15)




#Write a Python function that accepts a string and calculate the number 
# of upper case letters and lower case letters.


# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# string_test('The quick Brown Fox')




#Write a Python function that takes a list and returns a new list with 
# unique elements of the first list. 


# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(unique_list([1,2,3,3,3,3,4,5])) 




#Write a Python function that takes a number as a parameter and 
# check the number is prime or not.



# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(9))





 




