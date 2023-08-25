import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
        
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
        
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("comp turn: Rock(r) Paper(p) or Scissor(s)? ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'


you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)? ")
a = gameWin(comp, you)

print(f"COMPUTER CHOSE {comp}")
print(f"YOU CHOSE {you}")


if a == None:
    print("THE GAME IS A TIE")
elif a:
    print("YOU WIN")
else:
    print("YOU LOSE!")