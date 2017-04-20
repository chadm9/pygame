import pygame

pygame.init()

screen = {"height": 512, "width": 480}

keys = {"right": 275, "left": 276, "up": 273, "down": 274}

hero = {'x': 100, 'y': 100, 'speed': 10}


screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/background.png')

hero_image = pygame.image.load('images/hero.png')


game_on = True

while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        elif event.type == pygame.KEYDOWN:
            if event.key == keys["up"]:
                hero['y'] -= hero['speed']  
            if event.key == keys["down"]:
                hero['y'] += hero['speed'] 
            if event.key == keys["left"]:
                hero['x'] -= hero['speed'] 
            if event.key == keys["right"]:
                hero['x'] += hero['speed'] 

#Render
    pygame_screen.blit(background_image, [0,0])
    pygame_screen.blit(hero_image, [hero['x'], hero['y']])

    pygame.display.flip()
