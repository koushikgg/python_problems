import random
def snake_ladder():
    winning_position=100
    player_position=0
    def roll_dice():
        return random.randint(1, 6)

    def play_option():
        dice_value = roll_dice()
        option = random.choice(['no-play', 'ladder', 'snake'])
        return option, dice_value
            
    def game():
            start_position = 0
            player_position = start_position

            while player_position < winning_position:
                input("Hit 'enter' to roll the dice ") 

                play, dice_number = play_option()
                
                if play == 'no-play':
                    print("No Play")
                elif play == 'snake':
                    player_position -= dice_number
                    print("Oops Snake")
                else:  # option == 'ladder'
                    player_position += dice_number
                    print("You got a ladder")

                if player_position < 0:
                    count = 0
                    player_position = start_position
                    print("Restart Game")
                    count += 1
                    if count > 3:
                        return "You Lost "
                if player_position == winning_position:
                    return "Congrats you won"

                print(f"you got dice value : {dice_number}, now your at {player_position}")

   
    result = game()
    print(result)
    
snake_ladder()
