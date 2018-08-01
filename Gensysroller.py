import random

# Lists of dice and their possible outcomes
boost = ['','','X','XA','AA','A']
setback = ['','','F','F','T','T']
ability = ['','X','X','XX','A','A','XA','AA']
difficulty = ['','F','FF','T','T','T','TT','FT']
proficiency = ['','X','X','XX','XX','A','XA','XA','XA','AA','AA','TP']
challenge = ['', 'F', 'F', 'FF', 'FF', 'T', 'T', 'FT', 'FT', 'TT', 'TT', 'DR']


class GenesysDiceRoller:
    __success = 0
    __failure = 0
    __advantages = 0
    __threat = 0
    __triump = 0
    __dispair = 0
    __netSuccess = 0
    __netAdvantages = 0
    __displayDiceRolled = []

    def __init__(self,diceArray):
        self.bdice = diceArray[0]   # BOOST
        self.sdice = diceArray[1]   # SETBACK
        self.adice = diceArray[2]   # ABILITY
        self.ddice = diceArray[3]   # DIFFICULTY
        self.pdice = diceArray[4]   # PROFICIENCY
        self.cdice = diceArray[5]   # CHALLENGE

    def displayResults(self):
        rolled = 'Dice Rolled => (B/S/A/D/P/C):({}/{}/{}/{}/{}/{})'.format\
            (self.bdice,self.sdice,self.adice,self.ddice,self.pdice,self.cdice)
        print(rolled)
        # Following functions will roll the actual dice
        self.__rollDice(self.bdice, boost)  # BOOST
        self.__rollDice(self.sdice, setback)  # SETBACK
        self.__rollDice(self.adice, ability)  # ABILITY
        self.__rollDice(self.ddice, difficulty)  # DIFFICULTY
        self.__rollDice(self.pdice, proficiency)  # PROFICIENCY
        self.__rollDice(self.cdice, challenge)  # CHALLENGE


        # PRINT OUT RESULTS
        print("You rolled the following => ", self.__displayDiceRolled)
        print("Detailed Results")
        print("Successes = ", str(self.__success))
        print("Advantages = ", str(self.__advantages))
        print("Failures = ", str(self.__failure))
        print("Threats = ", str(self.__threat))
        print("Triumps = ", str(self.__triump))
        print("Displair = ", str(self.__dispair))


    def __rollDice(self, times, type):
        if (times != 0):
            for times in range(1, times + 1):
                dice = random.randint(0, len(type) - 1)
                rolled = type[dice]
                self.__determineResults(rolled)

    def __determineResults(self, rolled: object) -> object:
        self.__displayDiceRolled.append(rolled)
        if (rolled == ''):
            return
        elif (rolled == 'X'):
            self.__success += 1
        elif (rolled == 'XX'):
            self.__success += 2
        elif (rolled == 'XA'):
            self.__success += 1
            self.__advantages += 1
        elif (rolled == 'A'):
            self.__advantages += 1
        elif (rolled == 'AA'):
            self.__advantages += 2
        elif (rolled == 'F'):
            self.__failure += 1
        elif (rolled == 'FF'):
            self.__failure += 2
        elif (rolled == 'FT'):
            self.__failure += 1
            self.__threat += 1
        elif (rolled == 'T'):
            self.__threat += 1
        elif (rolled == 'TT'):
            self.__threat += 2
        elif (rolled == 'TP'):
            self.__triump += 1
            self.__success += 1
        elif (rolled == 'DR'):
            self.__dispair += 1
            self.__failure += 1
        # COMPUTE NET INFORMATION
        self.__netAdvantages = (self.__advantages - self.__threat)
        self.__netSuccess = (self.__success - self.__failure)
