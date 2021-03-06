import random
from enum import Enum
import os
from copy import deepcopy

SIZE = 5

class CardType5(Enum):
    TEAM1 = 9
    TEAM2 = 8
    BLACK = 1
    GRAY = 7

class CardType4(Enum):
    TEAM1 = 8
    TEAM2 = 7
    BLACK = 1
    GRAY = 4

#Card class
class Card:
    #initializes
    def __init__(self, img, typeOfCard, guessed, words):
        self.img = img
        self.typeOfCard = typeOfCard
        self.guessed = guessed
        self.words = words
        

    def __repr__(self):  
        return "[Image:% s Color:% s, % s, % s]" % (self.img, self.typeOfCard, self.guessed, self.words)
    
    #prints the card's image name
    # def printWord(self):
    #     print('{0: ^15}'.format(self.img), end="")

    # def printType(self):
    #     print('{0: ^15}'.format(self.typeOfCard), end = "")
        
    

def getImgPath(imgName):
    return os.path.join(getImgDirectory(),imgName)
    
def getImgDirectory():
    path = os.getcwd() 
    parent = os.path.dirname(path) 
    return os.path.join(parent, 'output')
    

def loadImageSet():
    image_set = os.listdir(getImgDirectory())
    return image_set

def loadWordSet():
    path = os.getcwd() 
    parent = os.path.dirname(path) 
    file = os.path.join(parent, 'output.txt')

    words = []
    with open(file) as f:
        for line in f:
            for word in line.split(','):
                words.append(word.strip())
    
    return words
        
def selectCards(sizeVal, ratio):
	
    chosenCards = []
    if sizeVal == 4:
        NUM_CARDS = 20
    elif sizeVal == 5:
        NUM_CARDS = 25
    
    noWords = int(NUM_CARDS * ratio)
    noPics  = NUM_CARDS - noWords
    
    word_set = loadWordSet()
    pic_set  = loadImageSet()
    
    randNumsWords = random.sample(range(len(word_set)), noWords)
    randNumsPics  = random.sample(range(len(pic_set)), noPics)
    
    full_set = []
    for word in randNumsWords:
        full_set.append((word_set[word], True))
        
    for pic in randNumsPics:
        full_set.append((pic_set[pic], False))
    
    random.shuffle(full_set)
    
    index = 0
    if sizeVal == 5:
        for i in CardType5:
            num = i.value
            while num > 0:
                chosenCards.append(Card(full_set[index][0],i.name, False, full_set[index][1]))
                num -= 1
                index += 1
    elif sizeVal == 4:
        for i in CardType4:
            num = i.value
            while num > 0:
                chosenCards.append(Card(full_set[index][0],i.name, False, full_set[index][1]))
                num -= 1
                index += 1
    
    random.shuffle(chosenCards)
    return chosenCards

def newGame(sizeVal, ratio = 0): #ratio is words to pictures, 0 means no words
    cardSet = selectCards(sizeVal, ratio)
    board = [[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    if sizeVal == 5:
        board.append([0,0,0,0,0])
    i = 0
    
    

    for i in range(0, sizeVal):
        for j in range(0,5):
            board[i][j] = cardSet[i*5 + j]
    # for cards in cardSet:
    #     board[i//SIZE][i%SIZE] = cards
    #     print((i//SIZE),i%SIZE, cards)
    #     i = i + 1
    return board
    
def getCleanBoard(board): #Returns board without anything in it
    newBrd = deepcopy(board)

    for row in newBrd:
        for card in row:
            if card.guessed == False:
                card.typeOfCard = 'GRAY'
            
    return newBrd