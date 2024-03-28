import pygame

from models import *
from engine import *

pygame.init()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Space Octopus")

gameEngine = PathEngine()

board = pygame.image.load("images/board.png")
board = pygame.transform.scale(board, (500, 500))

focus = pygame.image.load('images/focus.png')

def centredCoords(image, coords):
    x = coords[0]
    y = coords[1]
    new_x = x - (image.get_width()/2) 
    new_y = y - (image.get_height()/2)
    return (new_x, new_y)

def renderGame(window, gamestate):
    font = pygame.font.SysFont('centurygothic', 30, True)
    title = pygame.font.SysFont('centurygothic', 50, True)
    

    if gamestate == GameState.PAUSED:
        window.fill((128, 128, 128))

        text = font.render("1. Use keys 'A' and 'D' to select a tile", True, (255, 255, 255))
        x,y = font.size("1. Use keys 'A' and 'D' to select a tile")
        window.blit(text, (100, 230))
        text = font.render("2. Use the arrow keys <- and -> to rotate selected tile", True, (255, 255, 255))
        x,y = font.size("2. Use the arrow keys <- and -> to rotate selected tile")
        window.blit(text, (100, 280))
        text = font.render("3. Hover your mouse over the desired board space,", True, (255, 255, 255))
        x,y = font.size("3. Hover your mouse over the desired board space,")
        window.blit(text, (100, 330))
        text = font.render("and then press space to place selected tile.", True, (255, 255, 255))
        x,y = font.size("and then press space to place selected tile.")
        window.blit(text, (100, 380))

        text = title.render('MENU', True, (255, 255, 255))
        x,y = title.size('MENU')
        window.blit(text, (512 - (x/2), 100))

        text = font.render('PRESS SPACE TO PLAY', True, (255, 255, 255))
        x,y = font.size('PRESS SPACE TO PLAY')
        window.blit(text, (512 - (x/2), 500))

        text = font.render('PRESS ESC TO PAUSE', True, (255, 255, 255))
        x,y = font.size('PRESS ESC TO PAUSE')
        window.blit(text, (512 - (x/2), 575))

        text = font.render('PRESS R TO RESTART', True, (255, 255, 255))
        x,y = font.size('PRESS R TO RESTART')
        window.blit(text, (512 - (x/2), 650))


    elif gamestate == GameState.PLAYING:
        window.fill((128,128,128))

        window.blit(board, (290, 100))
        for tile in gameEngine.board.playedTiles:

            image = tile[0].image
            new_x = tile[1][0] - (image.get_width()/2) 
            new_y = tile[1][1] - (image.get_height()/2)
            window.blit(image, (new_x, new_y))
        
        i = 0
        for tile in gameEngine.player1.hand:
            if gameEngine.currentPlayer == gameEngine.player1 and gameEngine.player1.current_card == i/100:
                window.blit(focus, (58, 115 + i))
            window.blit(tile.image, centredCoords(tile.image, (100, 150 + i)))
            i = i + 100

        i = 0
        for tile in gameEngine.player2.hand:
            if gameEngine.currentPlayer == gameEngine.player2 and gameEngine.player2.current_card == i/100:
                window.blit(focus, (302 + i, 669))
            window.blit(tile.image, centredCoords(tile.image, (340 + i, 700)))
            i = i + 100

        i = 0
        for tile in gameEngine.player3.hand:
            if gameEngine.currentPlayer == gameEngine.player3 and gameEngine.player3.current_card == i/100:
                window.blit(focus,  (902, 109 + i))
            window.blit(tile.image, centredCoords(tile.image, (950, 150 + i)))
            i = i + 100 
        text = font.render('STARS: ' + str(gameEngine.player1.score), True, (255, 255, 255))
        window.blit(text, (45, 59))

        text = font.render('STARS: ' + str(gameEngine.player2.score), True, (255, 255, 255))
        window.blit(text, (493, 616))

        text = font.render('STARS: ' + str(gameEngine.player3.score), True, (255, 255, 255))
        window.blit(text, (877, 49))

run = True
while run: 
    key = None;
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and gameEngine.state == GameState.PLAYING:
            gameEngine.state = GameState.PAUSED
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and gameEngine.state == GameState.PAUSED:
            gameEngine.state = GameState.PLAYING
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and gameEngine.state == GameState.PAUSED:
            gameEngine = PathEngine()
            gameEngine.state = GameState.PLAYING
        elif event.type == pygame.KEYDOWN:
            key = event.key
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pos)

    gameEngine.play(key, pos)
    renderGame(window, gameEngine.state)
    pygame.display.update()

