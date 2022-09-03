import random
from time import sleep
from clr import clr
import os
#print("TOTP Time-based One Time Password")
clr()
def score_board(points):
    print(" " * 160, f"Score:|  {points}  |")
    return
def drill(prompt,answer, score):

    for i in range(1):
        
        clr()
        score_board(score)

        print("\n" * 23)
        print(" " * 93, f"{answer}")
        
        os.system(f"spd-say '{answer}'")
        sleep(3)
        clr()
        return

def main():
    score = 0
    with open("linux+.txt") as file:
        input_words = file.readlines()
    random.shuffle(input_words)
    
    for i in input_words:
        score_board(score)
        print("\n" * 23)
        current_couple = i.split(" ", 1)
        print(" " * 94, current_couple[0], "\n")
        inputs = input(" " * 95)
        
        if inputs == "exit":
            clr()
            score_board(score)
            print("\n" * 23)
            os.system(f"spd-say 'wtf'")
            print(" " * 95, f"fuck yeah!")
            sleep(1)
            clr()
            exit()

        if inputs == "remove":
            clr()
            score_board(score)
            print("\n" * 23)
            print(" " * 95, f"Removed from current list.")
            sleep(2)
            clr()
            break

        line = current_couple[1].strip("\n")
        line.strip("-")
        line.strip(",")
        lineout = line.lower()

        if inputs == lineout:
            score += 1
            clr()
            score_board(score)
            print("\n" * 23)
            os.system(f"spd-say 'fuck yeah!'")
            print(" " * 95, f"fuck yeah!")
            sleep(2)
            clr()
            continue

        if inputs != current_couple[1]:
            drill(current_couple[0], current_couple[1], score)
            clr()    

if __name__ == '__main__':
    
    main()
    

