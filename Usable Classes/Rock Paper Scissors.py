import random

choice = ('Rock', 'Paper', 'Scissors')
win_counter = 0
lose_counter = 0

while True:
    opponent_choice = choice[random.randint(0, 2)]
    print('Welcome to Rock, Paper, Scissors!!!')
    entry = input('''Please choose an option!
    1. Rock
    2. Paper
    3. Scissors
    4. EXIT
    ''').lower().strip()

    if entry == 'rock' or entry == '1':
        print('You chose... Rock!!')
        print(f'Your opponent chose... {opponent_choice}!!')
        if opponent_choice == "Rock":
            print('You TIED!!!')
        elif opponent_choice == 'Paper':
            print('Your LOSE!!!')
            lose_counter += 1
        elif opponent_choice == 'Scissors':
            print('You WIN!!!')
            win_counter += 1
    elif entry == 'paper' or entry == '2':
        print('You chose... Paper!!')
        print(f'Your opponent chose... {opponent_choice}!!')
        if opponent_choice == "Rock":
            print('You WIN!')
            win_counter += 1
        elif opponent_choice == 'Paper':
            print('You TIED !!!')
        elif opponent_choice == 'Scissors':
            print('You LOSE!!!')
            lose_counter += 1
    elif entry == 'scissors' or entry == '3':
        print('You chose... Scissors!!')
        print(f'Your opponent chose... {opponent_choice}!!')
        if opponent_choice == "Rock":
            print('You LOSE!!!')
            lose_counter += 1
        elif opponent_choice == 'Paper':
            print('You WIN!!!')
            win_counter += 1
        elif opponent_choice == 'Scissors':
            print('You TIED!!!')

    elif entry == 'quit' or entry == '4':
        break
    else:
        print('Please choose a correct choice!!!')

    if win_counter == 0 or win_counter > 1:
        print(f"\tYou've won {win_counter} turns!!!")
    elif win_counter ==1:
        print(f"\tYou've won {win_counter} turn!!!")

    if lose_counter == 0 or lose_counter > 1:
        print(f"\tYou've lost {lose_counter} turns =(")
    elif lose_counter == 1:
        print(f"\tYou've lost {lose_counter} turn =(")
