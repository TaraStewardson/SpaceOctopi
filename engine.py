from enum import Enum
import pygame
from models import *

class GameState(Enum):
    PAUSED = 0
    PLAYING = 1

class PathEngine:
    deck = None
    player1 = None
    player2 = None
    player3 = None
    board = None
    state = None
    currentPlayer = None
    result = None

    def __init__(self):
        self.player1 = Player("PURPLE", pygame.K_a, pygame.K_d, pygame.K_SPACE)
        self.player2 = Player("BLUE", pygame.K_a, pygame.K_d, pygame.K_SPACE)
        self.player3 = Player("ORANGE", pygame.K_a, pygame.K_d, pygame.K_SPACE)
        self.deal()
        self.board = Board()
        self.currentPlayer = self.player1
        self.state = GameState.PAUSED

    def deal(self):
        for i in range(0,5):
            self.player1.draw()
            self.player2.draw()
            self.player3.draw()

    def switchPlayer(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        elif self.currentPlayer == self.player2:
            self.currentPlayer = self.player3
        else:
            self.currentPlayer = self.player1

    def play(self, key, cursor_pos):
        if key == None:
            return
        
        if key == self.currentPlayer.selectkey:   
            score = self.board.addTile(self.currentPlayer.hand[self.currentPlayer.current_card], cursor_pos)
            if score:
                print(f"Current score: {self.currentPlayer.score}")
                print("Scored!")
                
                self.currentPlayer.collect_star()
            self.currentPlayer.play()
            self.currentPlayer.draw()
            self.switchPlayer()

        if key == self.currentPlayer.leftkey:
            self.currentPlayer.move_left()

        if key == self.currentPlayer.rightkey:
            self.currentPlayer.move_right()

        if key == pygame.K_RIGHT:
            self.currentPlayer.hand[self.currentPlayer.current_card].rotate_right()

        if key == pygame.K_LEFT:
            self.currentPlayer.hand[self.currentPlayer.current_card].rotate_left()


