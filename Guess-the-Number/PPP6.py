# MULTIPLAYER GUESSING GAME
import random
import time
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
def guess(x, y):
    # generates random number between the given range
    r = random.randrange(x, y)
    i = 0
    while True:
        c = int(input("Enter your guess: "))
        if c != r:
            print('Incorrect Guess!!')
            i = i + 1
        elif c == r:
            print("Correct Guess!!")
            no = i + 1
            print(f"\nYou took {no} chances")
            break
if __name__ == '__main__':
    initial1 = time.time()
    print("\nPlayer 1:\n")
    guess(a, b)
    total1 = time.time() - initial1
    initial2 = time.time()
    print("\nPlayer 2:\n")
    guess(a, b)
    total2 = time.time() - initial2
    print()
    # Who will be the winner
    if total1>total2:
        print("Player 2 Won!")
    elif total2>total1:
        print("Player 1 won!!")