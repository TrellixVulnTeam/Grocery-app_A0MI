import random

class NumberGame:
    def re_start_game():
        go_again = input('''
Want to go again?
Enter y or n
        ''')
        if go_again == 'y':
            start_game()
            the_game()
        else:
            print('Okay cool!')

    def start_game():
        print('''
----------------------------------------
Welcome to a number guessing game!
----------------------------------------
        
Rules:
* Pick a number between 1 - 10 and Algalon will tell you if if it's correct!
        
        ''')

    def the_game():
        choice = random.choice(range(1, 10))
        i = 0
        while True:
            Guess = int(input("Pick a number between 1 to 10 "))
            i += 1
            if Guess > choice:
                print("A little lower!")

            elif Guess < choice:
                print("A little higher!")
            else:
                print("You got it! The answer is {}. It took you {} tries".format(choice, i))

                return True
                break



    start_game()
    the_game()
    return_the_game = the_game()
    if the_game() == True:
        re_start_game()
    else:
        print("yolo")
