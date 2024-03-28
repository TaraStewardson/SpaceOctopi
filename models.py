from enum import Enum
import pygame
import random

class TileTypes(Enum):
    STRAIGHT = 0
    SHARP_TURN = 1
    GENTLE_TURN = 2
    TWO_ONE = 3
    ONE_ONE_ONE = 4
    THREE = 5

class Tile:
    type = None
    image = None
    color = None
    star = None
    rotation = None

    def __init__(self, type, color, star):
        self.type = type
        self.color = color
        self.star = star
        self.rotation = 0
        image = 'Images/' + self.type.name + "-" + str(self.color)
        if star:
            image = image + "-STAR"
      
        self.image = pygame.image.load(image + '.png')

    def rotate_right(self):
        self.image = pygame.transform.rotate(self.image, 60)

    def rotate_left(self):
        self.image = pygame.transform.rotate(self.image, -60)
        

class Deck:
    color = None

    def __init__(self, color):
        self.color = color

    def deal(self):
        type = random.choice(list(TileTypes))
        star = random.choice([True,False])
        return Tile(type, self.color, star)
    
    def length(self):
        return len(self.cards)

class Player:
    hand = None
    color = None
    deck = None
    current_card = None
    score = None

    def __init__(self, color, leftkey, rightkey, selectkey):
        self.color = color
        self.hand = []
        self.leftkey = leftkey
        self.rightkey = rightkey
        self.selectkey = selectkey
        self.deck = Deck(color)
        self.current_card = 0
        self.score = 0
        
    def draw(self):
        self.hand.append(self.deck.deal())
    
    def play(self):
        self.hand.pop(self.current_card)
    
    def move_right(self):
        if self.current_card != (len(self.hand)-1):
            self.current_card = self.current_card + 1

    def move_left(self):
        if self.current_card != 0:
            self.current_card = self.current_card - 1

    def collect_star(self):
        self.score = self.score + 1

class Board:
    playedTiles = None
    cols = None
    odd_rows = None
    even_rows = None

    def __init__(self):
        self.playedTiles = []
        self.cols = [340, 405, 468, 539, 606, 671, 740]
        self.rows = [[268, 353, 435],[228, 309, 389, 476],[187, 268, 353, 435, 516],[149, 228, 309, 389, 476, 560],[187, 268, 353, 435, 516],[228, 309, 389, 476], [268, 353, 435]]

    def addTile(self, tile, pos):
        score = 0

        # locate nearest slot
        x = pos[0]
        y = pos[1]

        cols_diff = []
        for col in self.cols:
            cols_diff.append(abs(col - x))
        index = cols_diff.index(min(cols_diff))
        new_x = self.cols[index]
        rows_diff = []
        rows = self.rows[index]
        for row in rows:
            rows_diff.append(abs(row - y))
        index = rows_diff.index(min(rows_diff))
        new_y = rows[index]

        ## check if a tile currently underneath
        underneath = False
        for playedTile in self.playedTiles:
            if playedTile[1] == (new_x, new_y):
                print("Tile underneath located")
                underneath = True
                self.playedTiles.remove(playedTile)
                print(playedTile[0].star)
                if playedTile[0].star:
                    score += 1

        if not underneath:# ie first tile placed
            if (new_x, new_y) == (539, 309) or (new_x, new_y) == (539, 389) or (new_x, new_y) == (468, 353) or (new_x, new_y) == (606, 353): # and on a tile on the board with a star
                score += 1

        self.playedTiles.append((tile, (new_x, new_y)))
        print(f"Score: {score}")
        return score





