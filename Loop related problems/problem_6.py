player_1 = int(input())
player_2_tries = int(input())

for i in range(player_2_tries - 1, -1, -1):
    player_2 = int(input())
    if player_1 != player_2:
        print(f'Wrong, {i} Choice(s) Left!')
    else:
        print('Right, Player-2 wins!')
        break
else:
    print('Right, Player-1 wins!')
    
# Question format

player_1 = int(input())
player_2_tries = int(input())

player_2_guesses = list(map(int, input().split()))

for i in range(player_2_tries - 1, -1, -1):
    correct_guess = False
    for guess in player_2_guesses:
        if guess == player_1:
            print('Right, Player-2 wins!')
            correct_guess = True
            break
    if not correct_guess:
        print(f'Wrong, {i} Choice(s) Left!')
else:
    print('Player-1 wins!')


