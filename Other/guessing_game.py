from random import randint
from time import sleep

first = 1
last = 1000
first_prompt = f"\n>> Welcome to guessing game, I'm thinking of a number between {first} and {last}, try to find it\n>> Press ^C to exit\n>> Good luck!\n>> "
correct_response = ">> Correct!\n>> See you later, come back soon!"
higher_response = ">> Higher!\n>> "
lower_response = ">> Lower!\n>> "
value_error_response = ">> Only numbers!"
exit_response = "\n>> See you soon!"

correct = randint(first, last)
response = first_prompt

def check_for_succes():
    global response
    if number < correct:
        response = higher_response
    elif number > correct:
        response = lower_response
    else:
        response = correct_response
        print(response)
        sleep(3)
        exit()

while True:
    try:
        try:
            number = int(input(response))
            check_for_succes()
        except ValueError:
            print(value_error_response)
    except KeyboardInterrupt:
        print(exit_response)
        exit()