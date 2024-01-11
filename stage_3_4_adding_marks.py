import random


def multiply():
    number = 0
    right = 0
    wrong = 0
    while number < 6:
        lst = ['-', '+', '*']
        a = int(random.randrange(2, 10))
        b = int(random.randrange(2, 9))
        c = random.choice(lst)

        result = eval(f"{a}{c}{b}")
        number += 1
        while True:
            try:
                print(f"{a} {c} {b}")
                user_input = eval(input())
                if user_input == result:
                    print("Right")
                    right += 1
                    break
                else:
                    print("Wrong")
                    wrong += 1
                    break
            except (SyntaxError, ValueError):
                print("Incorrect format")
    result = number - wrong
    print(f"Your mark is {result}/{number}")

multiply()