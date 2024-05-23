import random
choosing = True
while choosing:
    difficulty = input("Please select difficulty! Type normal or hard:")
    if difficulty == "normal":
        LIVES = 10
        choosing = False
    elif difficulty == "hard":
        LIVES = 5
        choosing = False
    else:
        print("You type wrong! please try again")

print("Welcome to the guessing number game")
print("I am thinking a number between 1 and 100")
game_running = True
NUMBER = random.randint(1, 100)
# print(NUMBER)
while game_running:
    number_choice = int(input("Make a Guess:"))
    if number_choice > NUMBER:
        print("Too high")
        LIVES -= 1
        print(f"You have {LIVES} lives left")
    if number_choice < NUMBER:
        print("Too low")
        LIVES -= 1
        print(f"You have {LIVES} lives left")
    if number_choice == NUMBER:
        print(f"You got it the number is {NUMBER}")
        game_running = False
    if LIVES == 0:
        game_running = False
        print(f"You lose, the number was:{NUMBER}")
