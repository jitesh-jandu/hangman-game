# it is a simple hangman game in which you have to guess the name

import random 

let = []

# only for visiters this list of name is taken from ai. rest full code is written by myself. thank you. !  

lis =["coffee","happy","game","snake","guess""monkey", "tiger", "rabbit", "parrot", "giraffe", "zebra", "camel", "dolphin", 
    "penguin", "elephant", "kitten", "puppy", "spider", "turtle", "lizard", "donkey",
    "apple", "banana", "mango", "orange", "potato", "carrot", "lemon", "grapes", 
    "cherry", "tomato", "onion", "garlic", "papaya", "melon","pencil", "bottle", "camera", "pillow", "clock", "chair", "mirror", "window", 
    "blanket", "wallet", "jacket", "guitar", "hammer", "bucket", "candle", "laptop",
    "summer", "winter", "shadow", "flower", "garden", "jungle", "cloud", "forest", 
    "river", "desert", "rainbow", "planet", "island", "valley","school", "doctor", "pirate", "wizard", "monster", "dragon", "market", "castle", 
    "palace", "police", "driver", "baker", "pilot", "farmer","bicycle", "soccer", "cricket", "rocket", "airplane", "scooter", "runner", "player", 
    "tennis", "hockey","happy", "coffee", "cinema", "dinner", "butter", "cheese", "cookie", "family", 
    "friend", "window", "yellow", "purple", "silver", "golden", "basket", "travel" ]

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
