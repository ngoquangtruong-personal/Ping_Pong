import pygame

from define import *
from player import PLAYER
from ball import BALL

pygame.init()

# Images
imageIcon = pygame.image.load(PATH_DIRECTORY_IMAGES + '/Icon.png')
imageBackground = pygame.image.load(PATH_DIRECTORY_IMAGES + '/Background.png')
imageBall = pygame.image.load(PATH_DIRECTORY_IMAGES + '/Ball.png')
imagePlayerLeft = pygame.image.load(PATH_DIRECTORY_IMAGES + '/Player_left.png')
imagePlayerRight = pygame.image.load(PATH_DIRECTORY_IMAGES + '/Player_right.png')
imageScoreBoard = pygame.image.load(PATH_DIRECTORY_IMAGES + '/Score_board.png')

# Sound
soundBackground = pygame.mixer.Sound(PATH_DIRECTORY_SOUNDS + '/Background_music.mp3')
soundWinning = pygame.mixer.Sound(PATH_DIRECTORY_SOUNDS + '/Winning.mp3')
soundBallOnPlayer = pygame.mixer.Sound(PATH_DIRECTORY_SOUNDS + '/Ball_collides_bare_floor.mp3')
soundBallOnWall  = pygame.mixer.Sound(PATH_DIRECTORY_SOUNDS + '/Ball_collides_player.mp3')

def keyEvents():
    global isRun
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerRight.moveUp()
            if event.key == pygame.K_DOWN:
                playerRight.moveDown()
            if event.key == pygame.K_w:
                playerLeft.moveUp()
            if event.key == pygame.K_s:
                playerLeft.moveDown()

def showScores():
    font = pygame.font.Font(PATH_DIRECTORY_FONTS + '/Rexliarg.otf', 25)
    scoreText = str(playerLeft.score) + ' : ' + str(playerRight.score)
    
    scoreSurface = font.render(scoreText, True, COLOR_WHITE)
    scoreWidth = scoreSurface.get_width()
    
    windowGame.blit(scoreSurface, (WINDOW_WIDTH / 2 - scoreWidth / 2, 0))

def checkWinnerPlayer():
    if ball.x + BALL_SIZE < 0:
        playerRight.score += 1
        ball.setPositon()
        pygame.mixer.Sound.play(soundWinning)

    if ball.x - BALL_SIZE > WINDOW_WIDTH:
        playerLeft.score += 1
        ball.setPositon()
        pygame.mixer.Sound.play(soundWinning)

def checkCollisionBallWithPlayer():
    if (ball.x - BALL_SIZE <= playerLeft.x + PLAYER_WIDTH) and (ball.y + BALL_SIZE > playerLeft.y) and (ball.y - BALL_SIZE < playerLeft.y + PLAYER_HEIGHT):
        ball.velocityX *= -1
        pygame.mixer.Sound.play(soundBallOnPlayer)

    if (ball.x + BALL_SIZE >= playerRight.x) and (ball.y + BALL_SIZE > playerRight.y) and (ball.y - BALL_SIZE < playerRight.y + PLAYER_HEIGHT):
        ball.velocityX *= -1
        pygame.mixer.Sound.play(soundBallOnPlayer)

def checkBallOnWall():
    if ball.y - BALL_SIZE <= 0 or ball.y + BALL_SIZE >= WINDOW_HEIGHT:
        pygame.mixer.Sound.play(soundBallOnWall)


pygame.display.set_caption('Ping Pong')
pygame.display.set_icon(imageIcon)
pygame.mixer.Sound.play(soundBackground)

windowGame = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Init player
playerLeft = PLAYER(imagePlayerLeft, 20, WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2)
playerRight = PLAYER(imagePlayerRight, WINDOW_WIDTH - PLAYER_WIDTH - 20, WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2)

# Init ball
ball = BALL(imageBall)

isRun = True
while isRun:
    pygame.time.delay(100)

    windowGame.blit(imageBackground, (0, 0))
    windowGame.blit(imageScoreBoard, (WINDOW_WIDTH / 2 - imageScoreBoard.get_width() / 2, 0))

    # Key events
    keyEvents()

    # Draw players
    playerLeft.show(windowGame)
    playerRight.show(windowGame)

    # Draw ball
    ball.show(windowGame)
    ball.run()

    # Check victory, defeat
    checkWinnerPlayer()

    # Check collision ball with player
    checkCollisionBallWithPlayer()

    # Check ball on wall
    checkBallOnWall()

    # Show score
    showScores()

    # Update interface
    pygame.display.update()

pygame.quit()