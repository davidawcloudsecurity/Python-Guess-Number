import random
# Guess The number
keep_going = True
tries = 1

def guess(user, machine_number):
    global tries
    if user > machine_number:
        print("Too high")
        tries += 1
        return True 
    elif user < machine_number:
        print("Too low")
        tries += 1
        return True
    else:
        print(f"You've guess it.\nYou took {tries}!")
        print("\nTry better next time") if tries > 2 else print("\nYou are awesome!")
        return False
    
     
limit = int(input("Please enter range: "))
machine_number = random.randint(1, limit)
print(f"machine: {machine_number}")
 
while keep_going:
    user_guess = int(input("Please guess the number: "))
    keep_going = guess(user_guess, machine_number)
