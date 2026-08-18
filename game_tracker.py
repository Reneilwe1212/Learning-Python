#while loop

while True:
    score = input("Enter your game score: ")


    if score.lower().split() == "stop":
        print("Game session ended!")
        break

    new_score = int(score)
if new_score > 100:
    print("Wow! That's a new high score")
        
else:
    print("Good try, keep playing!")
        #not done