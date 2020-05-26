import random

reroll = "yes"

while reroll:
    print ("Rolling the dice...")
    print (random.randint(1, 20))
    print("Roll again? (Press y to reroll)")
    reroll = "y" in input()
    
