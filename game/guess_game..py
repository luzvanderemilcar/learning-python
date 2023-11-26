# Guess Game
set_number = 9
guess_count = 0
max_turn = 3
while guess_count < max_turn:
    try:
        guess_number = int(input("Guess : "))
        guess_count += 1
        if guess_number == set_number:
            print("You Won !")
            break
        else:
            chance_remaining = max_turn - guess_count
            print(f'Chance Remaining : {chance_remaining}')
    except:
        print("Enter a valid number")
else:
    print("You fail !")
