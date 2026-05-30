# it is a simple hangman game in which you have to guess the name

import random 

let = []

lis =["coffee","happy","game","snake","guess" ]

name = random.choice(lis) 

hint = random.sample(range(len(name)),k = 2)



print("="*30)
print("welcome to hangman")
print("lets , play hangman")
print("-"*30)

life = 5

display = ["_"]*len(name)

for indox in hint :
    display[indox] = name[indox]



print(" ".join(display))

while life > 0 and "_" in display :
    found = False
    user = input("enter your guess alphabate:--")
    print("="*30)

    for i in range(len(name)) :
        

        leter = name[i]
        if user == leter:
          display[i] = user
          found = True

    if found == False :
        let.append(user)
        print("not match , please try another letter")
        life -= 1 
        print(f"you tries are :{let}")
        
             
    print(f"life lefi : {life}")

    print(" "*30)

    print(" ".join(display))

    

if not "_" in display :
    print("="*30)
    print("you win !")
    print(f"yes , your letter is {name} !")
    print(f"you still had {life}lives !")


    print("="*30)

elif life == 0 :
    print("="*30)
    print("sorry but you lose !")
    print(f"ohhho, your letter is {name} !")    
    print("="*30)

print("created by * jitesh jandu *")
print("="*30)
