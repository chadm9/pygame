# 1. Include pygame
# Include pygame which we got from pip
import pygame
from math import fabs
from random import randint

# in order to use pygame, we have to run the init method
# 2. Init pygame
pygame.init()


# 3. Create a screen with a size
screen = {
	"height": 512,
	"width": 480
}

keys = {
	"right": 275,
	"left": 276,
	"up": 273,
	"down": 274
}

keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False,
}

hero = {
	"x": 100,
	"y": 100,
	"speed": 10,
	"wins": 0,
        "lives": 3
}
  

goblin = {
        "x": 200,
        "y": 200,
        "speed": 1
}

monster = {
        "x": 300,
        "y": 300,
        "speed": 1
}

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('./images/background.png')
hero_image = pygame.image.load('./images/hero.png')
goblin_image = pygame.image.load('./images/goblin.png')
monster_image = pygame.image.load('./images/monster.png')

pygame.mixer.music.load('sounds/music.wav')
pygame.mixer.music.play(-1)


# /////////////////////////////////////////////
# //////////////MAIN GAME LOOP/////////////////
# /////////////////////////////////////////////	x
game_on = True
# Create the game loop (while 1)
while game_on:
	# we are inside teh main game loop. It will run as long as game_on is true
	# ---EVENTS!!----
	for event in pygame.event.get():
		# Looping through all events that happened this game loop cycle
		# 4. Add a quit event (requires sys)
		if event.type == pygame.QUIT:
			# the user clicked on the red X to leave the game
			game_on = False
			# update our boolean, so pygame can escape the loop
		elif event.type == pygame.KEYDOWN:
			if event.key == keys['up']:
				keys_down['up'] = True
			elif event.key == keys['down']:
				keys_down['down'] = True
			elif event.key == keys['left']:
				# print "User pressed left!"
				keys_down['left'] = True
			elif event.key == keys['right']:
				# print "User pressed right!"
				keys_down['right'] = True
		elif event.type == pygame.KEYUP:
			# print "The user let go of a key"
			if event.key == keys['up']:
				# the user let go of a key... and that key was the up arrow
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
			if event.key == keys['right']:
				keys_down['right'] = False

	# Update Hero position
	if hero['lives'] > 0:
	    if keys_down['up'] and hero['y'] > 0:
	   	    hero['y'] -= hero['speed']
	    elif keys_down['down'] and hero['y'] < 450:
		    hero['y'] += hero['speed']
	    if keys_down['left'] and hero['x'] > 0:
		    hero['x'] -= hero['speed']
	    elif keys_down['right'] and hero['x'] < 480:
		    hero['x'] += hero['speed']

        distance_between = fabs (hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
        if distance_between < 32:
            rand_x = randint(0, 480)
	    rand_y = randint(0, 450) 

	    goblin['x'] = rand_x
            goblin['y'] = rand_y
	    hero['wins'] += 1 
            goblin['speed'] +=1
            monster['speed'] +=1

        distance_between = fabs (hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])
        if distance_between < 32:
            rand_x = randint(0, 480)
            rand_y = randint(0, 450)

            monster['x'] = rand_x
            monster['y'] = rand_y
            hero['lives'] -= 1
	#if hero['lives'] == 0:
	    #exit() 
	# ---RENDER!---
	# blit takes 2 arguments
	# 1. What?
	# 2. Where?
	# Screen.fill (pass bg_color)
	if hero['lives'] > 0:
            if hero['x'] > monster['x']:
                monster['x'] += monster['speed']
        
            if hero['x'] < monster['x']:
                monster['x'] -= monster['speed']

            if hero['y'] > monster['y']:
                monster['y'] += monster['speed']

            if hero['y'] < monster['y']:
                monster['y'] -= monster['speed']

	if hero['lives'] > 0:
            if hero['x'] > goblin['x']:
                goblin['x'] -= goblin['speed']

            if hero['x'] < goblin['x']:
                goblin['x'] += goblin['speed']

            if hero['y'] > goblin['y']:
                goblin['y'] -= goblin['speed']

            if hero['y'] < goblin['y']:
                goblin['y'] += goblin['speed']
        
        if goblin['y'] >= 450:
	    goblin['y'] = 0 

        if goblin['y'] <= 0:
            goblin['y'] = 450   


        if goblin['x'] >= 480:
            goblin['x'] = 0

        if goblin['x'] <= 0:
            goblin['x'] = 480

	pygame_screen.blit(background_image, [0,0])

	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d   Lives: %d " % (hero['wins'], hero['lives']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])
	# draw the hero

	end_font = pygame.font.Font(None, 55)
	game_over = end_font.render('You Suk!  (git gud)', True, (0,0,0))
	if hero['lives']==0:
	    pygame_screen.blit(game_over, [90,130])

	pygame_screen.blit(hero_image, [hero['x'],hero['y']])

        pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])

        pygame_screen.blit(monster_image, [monster['x'], monster['y']])

	# clear the screen for next time
	pygame.display.flip()

