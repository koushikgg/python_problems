import random

def coin_flip(number_of_flips):
    heads = 0
    tails = 0
    for _ in range(number_of_flips):
        coin_toss = random.random()
        if coin_toss < 0.5 :
            tails += 1
        else:
            heads += 1
    head_percentage = (heads / number_of_flips) * 100
    tail_percentage = (tails / number_of_flips) * 100
    return head_percentage, tail_percentage

if __name__ == '__main__':
    number_of_flips = int(input("Enter number of coin flips: "))
    head_percentage, tail_percentage = coin_flip(number_of_flips)
    print(f'heads percentage is {head_percentage} and tails percentage is {tail_percentage}')