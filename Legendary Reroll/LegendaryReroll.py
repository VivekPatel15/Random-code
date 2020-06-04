# Made by Vivek Patel aka Vishnu
# Twitter: @HiImVishnu Discord: Vishnu#3379
# Made for DuncanCantDie and friends for RFFAs
# LegendaryReroll.py rolls for a random legendary Pokemon
# Reads from Legendaries.txt
# please edit or rename .txt files for future compatibility
import random

active = 'true'

def reroll():
    print(random.choice(list(open('Legendaries.txt'))))

while active:
    reroll()
    input('Press Enter to reroll\n')


