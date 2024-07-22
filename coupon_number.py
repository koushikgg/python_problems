import random

def coupon_number(num):
    coupons = set()
    random_numbers = 0
    while len(coupons) < num:
        coupon = random.randint(1, num)
        coupons.add(coupon)
        random_numbers += 1
    return random_numbers

number = int((input('Enter the number: ')))
output = coupon_number(number)
print(f"total {output} random number is needed to have all distinct numbers ")