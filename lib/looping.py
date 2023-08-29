#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    return [i * i for i in int_list]

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    

# # while loop in Python
# i = 0
# while i < 5:
#     print("Looping")
#     i += 1

# # for loop in Python
# for i in range(10):
#     print("Looping")
#     print(f"i is: {i}")

# # List Comprehensions 
# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# # using for loop
# inch_heights = list()
# for height in player_heights:
#     inch_height = height * 7920
#     inch_heights.append(inch_height)

# # using list comprehension
# inch_heights = [height * 7920 for height in player_heights]