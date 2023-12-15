######################
# CREATED BY ZAKLEBY #
######################

import random

activeGame = False

cardNumbers = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
cardTypes = ["HEARTS","DIAMONDS","SPADES","CLUBS"]

playerCards = []
computerCards = []

######################
# CREATED BY ZAKLEBY #
######################

def addCard(addToPlayer: bool):

    randomCardNum = cardNumbers[random.randint(0,len(cardNumbers)-1)]
    randomCardType = cardTypes[random.randint(0,len(cardTypes)-1)]
    card = f"{randomCardNum} OF {randomCardType}"

    if addToPlayer:
        if card in playerCards:
            addCard(True)
            return
    
        playerCards.insert(-1, card)

    else:
        if card in computerCards:
            addCard(False)
            return
    
        computerCards.insert(-1, card)

######################
# CREATED BY ZAKLEBY #
######################
        
def getScore(getPlayerScore: bool):
    total = 0
    nums = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    if getPlayerScore:
        for card in playerCards:
            card_value = card.split()[0]
            total = total + nums[card_value]

    else:
        for card in computerCards:
            card_value = card.split()[0]
            total = total + nums[card_value]

    return total

######################
# CREATED BY ZAKLEBY #
######################

def getCards(getPlayerCards: bool):

    final = ''

    if getPlayerCards:
        for card in playerCards:
            final = final + f"{card}\n"
    
    else:  
        for card in computerCards:
            final = final + f"{card}\n"
        
    return final

######################
# CREATED BY ZAKLEBY #
######################

def game():

    input('Press enter to start game')

    activeGame = activeGame = True
    standPlayer = False
    standComputer = False

    for i in range(2):
        addCard(True)
        addCard(False)
    
    print(f'Cards have been delt to both opponents. Your cards are:\n{getCards(True)}')

    while activeGame:
        if standPlayer == False:
            option = input(f'Your cards add up to {getScore(True)} and the computer has {len(computerCards)} cards. Would you like to "hit" or "stand" (h/s)? >> ')

        if option == 'h':
            addCard(True)
            
        elif option == 's':
            standPlayer = standPlayer = True

        if getScore(False) < 17 and getScore(False) > 14:

            randomNum = random.randint(1,2)
            if randomNum == 1 and standComputer == False:
                addCard(False)
                print(f'Computer chose "hit" and now has {len(computerCards)} cards')

            else:
                print(f"computer stand")
                standComputer = standComputer = True
        
        elif getScore(False) > 17 and standComputer == False:
            print("computer stand")
            standComputer = standComputer = True

        else:
            if standComputer == False: 
                addCard(False)
                print(f'Computer chose "hit" and now has {len(computerCards)} cards')
            
        if getScore(True) > 21:
            print(f"Computer won this round, you went over 21. Computer was on {getScore(False)}")
            break

        elif getScore(False) > 21:
            print("You won this round, the computer went over 21")
            break

        elif standComputer and getScore(False) < getScore(True):
            print('You won this round, computer stand on a lower number than you')
            break

        elif standPlayer and getScore(False) > getScore(True):
            print(f'Computer won this round, you stand on a lower number than the compute. Computer was on {getScore(False)}')
            break

        elif getScore(True) == 21:
            print("You won this round, you are exactly on 21!")
            break

        elif getScore(False) == 21:
            print("Computer won this round, they are exactly on 21")
            break

        continue

game()

######################
# CREATED BY ZAKLEBY #
######################