import random
def game():
    print ("Welcome to the game!")
    score = random.randint(1,50)
    with open("score.txt") as f:
        high_score = f.read()
        if (high_score!="") :
            high_score = int(high_score)
        else:
            high_score = 0
    print(f"Your score is: {score}")
    if (score > high_score):
        print("Congratulations! You have a new high score!")
        with open("score.txt", "w") as f:
            f.write(str(score))
    return score
game()
