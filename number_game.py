import random 
random.seed()

games_played=0

while True: 
    guesses=0
    k=random.randint(1,100)
    #print(k)
    
    while True:
        x= input("Enter your guess: ") 
        guesses=guesses+1
        x=int(x)
        if x==k:
            print("YAY! it took you", guesses, "guesses")
            break
        
        else:
            if x>k:
                print("too high")
            else: 
                print("too low")
    games_played=games_played+1
    c=input("Play again?")
    if c=="no": 
        print("bye")
        break
if games_played==1: 
print("done, you played", games_played, "game! good job!") 
else:
    if games_played>1:
        print("done, you played", games_played, "games! good job!")
    
    
    
