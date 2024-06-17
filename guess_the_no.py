import random

target=random.randint(1,100)


while True:
    user_choice=(input("Enter any no. btwn 1 to 100 \n if want to quit (Q) : "))
    
    if(user_choice=='Q'):
        print("Quitting the game.....")
        break
    user_choice=int(user_choice)
    if(user_choice==target):
        print("SUCCESS....CORRECT GUESS")
    elif(user_choice>target):
        print("YOUR NO. WAS TOOOOO BIGGG !!!!!")
    else:
        print("YOUR NO. WAS TOOOOO SMALLL !!!!")

print("_____GAME OVER____")