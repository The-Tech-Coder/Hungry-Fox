import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

egg = Actor("one-egg")
egg.pos = 200, 200

def draw():
    screen.fill("blue")
    fox.draw()
    egg.draw()
    screen.draw.text("Score: " + str(score), topleft=(10, 10))
    
    if game_over:
        screen.fill("yellow")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60, color="black")

def place_egg():
    egg.x = randint(20, (WIDTH - 20))
    egg.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2
    
    
    egg_collected = fox.colliderect(egg)
    if egg_collected:
        score = score + 10
        place_egg()
        
clock.schedule(time_up, 10.0)
place_egg()
pgzrun.go()
