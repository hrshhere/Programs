# import random

# a = random.randint(1, 10)
# b = random.randint(1, 10)

# answer = int(input(f"What is {a} times {b}? "))

# if answer == a*b:
#     print(f"Correct {a} times {b} is {answer}")

# else :
#     print(f"Incorrect {a} times {b} is {a*b}")




import random

print("Enter choice : 1 : Rock, 2 : Paper, 3 : Scissor")

choice = int(input("choice (1/2/3):"))

computer_choice = random.randint(1,3)
print(f"computer: {computer_choice}")

if choice == computer_choice:
    print("Draw")

elif choice == 1: 
    
    if computer_choice == 2:
        print("computer wins")

    else :
        print("you win")

elif choice == 2:
    if computer_choice == 1:
        print("you win")
    else :
        print("computer wins")

elif choice == 3:
    if computer_choice == 1:
        print("computer wins")
    else : 
        print("you win")


