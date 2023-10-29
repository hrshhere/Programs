# import random
# from secrets import choice

# words = ['father','mother','son','daughter','sister','uncle','aunty','brother','grandfather','grandmother']
# word = random.choice(words)

# print(word)







# a = int(input("enter number"))

# for i in range(1,11):
#     i = a*i
#     print(i)



# fastfood = ["pizza","burgure","paav","freinky","fries","momos"]

# for name in fastfood:
#     if name.startswith("f"):
#         print("Hello " + name)






# n = int(input("Enter Number "))

# prime = True 

# for i in range(2,n):
#     if(n%i) == 0:
#         prime = False

#         break 

# if prime:
#     print("this number is prime")


# else:
#     print("this number is not prime")




# n = int(input("enter number"))
# f = 1

# for i in range(1,n+1):
#     f = f*i

# print("factorial of", n ,"is =",f)





# n = 3

# for i in range(n):
#     print("*"*(i+1))






# n = int(input("enter number"))

# for i in range(10,0,-1):

#     i = n*i

#     print(i)






#-------simple pattern programme------------


# for i in range(0,5):
#      for c in range(0,5):
#         print("*",end= "")

#      print()







#--------Simple Pyramid Programme-----------


# n = 5


# for i in range(0, n):
     
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i+1):
         
#             # printing stars
#             print("* ",end="")
      
#         # ending line after each row
#         print("\r")
 




#--------After 180 degrees rotation-------



# n = 5

# for i in range(1,n):
#     print(" "*(n-i),"*"*(i))






#-------Printing Triangle-------


# n = 6

# for i in range(0,n):
#     print(" "*(n-i-1)+"*"*(2*i+1))

#     print()





# n = 5

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")

#     for k in range(2*i+1):
#         print("*",end="")

#     print()









# n = 5
    
    
# for i in range(n):
#     for k in range(2 * i + 1):
        
#         if k == 0 or k == 2 * i:
#             print('*', end='')
#         else:
#             if i == n - 1:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#     print()






# n = 5


# for i in range(5):
#     for j in range(n-i-1):
#         print(" ",end="")
 
#     for k in range (2*i+1):
        
#         if k == 0 or k == 2*i:
#             print("*",end="")

#         else:
#             if i == n - 1:
#                 print("*", end="")

#             else:
#                 print(" ", end="")
        
#     print() 

# 


# n = 5

# for i in range(5):
#     print(" "*(n-i-1) + "*"*(2*i+1) + " "*(n-i-1)
# 
# 
# 



# n = 5

# for i in range(5):

    #print("*"*(n),end="")-------pro

    # for j in range(5):
    #     print("*",end="")

    #print()





# n = 5

# for i in range(n):

#     #for j in range(n):

#     if i == 0 or i == n-1:
#         # j == 0 or j == n-1:
#         print("*"*n)

#     else:
#         print("*"+" "*(n-2)+"*")

# print()



# n = 5

# for i in range(0,n):

#     for j in range(0,i):

#         print("*",end="")

#     print()


# n = 5

# for i in range(0,n):

#     print("*"*i)

 # print()





# n = 5

# for i in range(n):

#     for j in range(0,n-i):
#         print(" ",end="")

#     for k in range(0,i+1):
#         print("*",end="")

#     print()



# n = 5

# for i in range(1,n+1):

#     print(" "* (n-i)+"*"*i)





#n = 5

# for i in range(n):

#     for j in range(n-i):

#         print("*",end="")

#     print()

# for i in range(n):

#     print("*"*(n-i))





# n = 5

# for i in range(n):

#     for j in range(i):
#         print(" ",end="")

#     for j in range(n-i-1):
#         print("*",end="")

#     print()





# size = 5
# for i in range(size):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(size, i, -1):
#         print("*", end="")
#     print()




# n = 6 

# for i in range(n+1):
#     for j in range(i):

#         if j == 0 or j == i-1:
#             print("*",end="")

#         else:

#             if i != n:
#                 print(" ",end="")

#             else:
#                 print("*",end="")

#     print()




# n = 5 
# for i in range(n):

    #print(" "*(n-i-1) + "*"*(2*i+1))



    
# n = 5
# for i in range(n):
#     # printing spaces
#     for j in range(n - i - 1):
#         print(' ', end='')

#     # printing stars
#     for k in range(2 * i + 1):
#         # print star at start and end of the row
#         if k == 0 or k == 2 * i:
#             print('*', end='')
#         else:
#             if i == n - 1:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#     print()









