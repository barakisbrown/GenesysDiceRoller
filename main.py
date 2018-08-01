from utils import inputNumberOrReturn
from Gensysroller import GenesysDiceRoller

# STATIC STRINGS
about = "Genesys Python Dice Roller by Matthew Brown, @2018"
question1 = "How many boost dice? (return for 0) => "
question2 = "How many setback dice (return for 0) => "
question3 = "How many Ability dice (return for 0) => "
question4 = "How many Difficulty dice (return for 0) => "
question5 = "How many Proficiency dice (return for 0) => "
question6 = "How many Challenge dice (return for 0) => "

# MAIN PART OF PROGRAM HERE
dice = []

print(about)

blue = inputNumberOrReturn(question1)
black = inputNumberOrReturn(question2)
green = inputNumberOrReturn(question3)
purple = inputNumberOrReturn(question4)
yellow = inputNumberOrReturn(question5)
red = inputNumberOrReturn(question6)

dice.append(blue)
dice.append(black)
dice.append(green)
dice.append(purple)
dice.append(yellow)
dice.append(red)

GenRolled = GenesysDiceRoller(dice)
GenRolled.displayResults()
#end of main area