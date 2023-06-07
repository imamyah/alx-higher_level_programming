#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ldigit = number % -10
else:
    ldigit = number % 10
print('Last digit of {} is '.format(number), end="")
if ldigit > 5:
    print('{} and is greater than 5'.format(ldigit))
elif ldigit == 0:
    print('{} and is 0'.format(ldigit))
elif ldigit < 6 and ldigit != 0:
    print('{} and is less than 6 and not 0'.format(ldigit))
