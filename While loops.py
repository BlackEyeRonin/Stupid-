# Type 1
import time
food = input('Enter your food name:') #Define what the constant is
while food == "":                            #Write the first condition
       print ("PLEASE ENTER YOUR FOOD NAME!") #1st condition's output
       food = input("Enter your food name:") #Go back to first function (repeating)

print(f"Nice that your fav food is {food}") #Final output 
time.sleep(3)


# Type 1.1 - Infinite loop (Refer file)

# Type 2 - Numerical

Credit_card_number = int(input("Enter your credit card number!"))
while Credit_card_number < 0 or Credit_card_number > 2000000000:
       print("ENTER BEFORE I HACK YOUR ACCOUNT!")
       Credit_card_number = int(input("Enter your credit card number:"))

print(f"Good, Now I can buy PS5 with your money, {Credit_card_number} is gonna be empty soon...")
time.sleep(3)


# Bonus - Guess Game
print("Think of a number")
num= int(input('Enter that number:'))
time.sleep(2)
input("Loading...Press Enter")
time.sleep(2)
input("Press Enter for the magic to happen...")
time.sleep(3)
print("The number you thought of was\n",time.sleep(3),num)
