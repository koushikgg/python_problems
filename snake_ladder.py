import random

def roll_dice():
    return random.randint(1, 6)

def play_option():
        dice_value = roll_dice()
        option = random.choice(['no-play', 'ladder', 'snake'])
        if option == 'no-play':
            return
        elif option == 'snake':
            player_position -= dice_value
            return player_position
        else: 
            player_position += dice_value
            return player_position

start_position=0