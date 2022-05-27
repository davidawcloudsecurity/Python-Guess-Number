import random
# Guess The number
keep_going = True

def guess(user, machine_number):
    if user > machine_number:
        print("Too high")
        return True
    elif user < machine_number:
        print("Too low")
        return True
    else:
        print("You've guess it")
        return False
    
     
limit = int(input("Please enter range: "))
machine_number = random.randint(1, limit)
print(f"machine: {machine_number}")
 
while keep_going:
    user_guess = int(input("Please guess the number: "))
    keep_going = guess(user_guess, machine_number)
