# STONE PAPER SCISSOR GAME
from playsound import playsound
loc = "Audio\\buzzersound.wav"
loc2 = "Audio\\right.mp3"
loc3 = "Audio\\Tie.wav"
import random
lst = ['stone', 'paper', 'scissor']
i = 0
player_point = 0
comp_point = 0
while i<10:
    i = i+1
    comp = random.choice(lst)
    player = input("Choose one; Stone, Paper, Scissor : ").lower()
    if player == "stone" and comp == "paper":
        print(f'Computer = {comp}')
        player_point = player_point + 1
        print("Player Won!!")
        print(f'PLAYER = {player_point} COMPUTER = {comp_point}')
        playsound(loc2)
    elif player == "stone" and comp == "scissor":
        print(f'Computer = {comp}')
        player_point = player_point + 1
        print("Player Won!!")
        print(f'PLAYER = {player_point} COMPUTER = {comp_point}')
        playsound(loc2)
    elif player == "paper" and comp == "scissor":
        print(f'Computer = {comp}')
        comp_point = comp_point + 1
        print("Computer Won!!")
        print(f'PLAYER = {player_point} COMPUTER = {comp_point}')
        playsound(loc)
    elif player == "scissor" and comp == "paper":
        print(f'Computer = {comp}')
        player_point = player_point + 1
        print("Player Won!!")
        print(f'PLAYER = {player_point} COMPUTER = {comp_point}')
        playsound(loc2)
    elif player == "paper" and comp == "stone":
        print(f'Computer = {comp}')
        comp_point = comp_point + 1
        print("Computer Won!!")
        print(f'PLAYER = {player_point} COMPUTER = {comp_point}')
        playsound(loc)
    elif player == "scissor" and comp == "stone":
        print(f'Computer = {comp}')
        comp_point = comp_point + 1
        print("Computer Won!!")
        playsound(loc)
        print(f'PLAYER = {player_point} COMPUTER = {comp_point}')
    elif player == comp:
        print(f'Computer = {comp}')
        print("Tie")
        playsound(loc3)
    else:
        i = i-1
        print("Enter a valid value")
# decides who is the winner
if player_point>comp_point:
    dif1 = player_point-comp_point
    print(f"\nPlayer Won by {dif1} points")
elif player_point<comp_point:
    dif2 = comp_point-player_point
    print(f"\nComputer Won by {dif2}")
elif player_point==comp_point:
    print(f"Tie!!")