import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initializing game
    pygame.init()
    
    # Setting screen mode, clock and delta time
    # dt is the time between frames
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Defining pygame groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Adding classes to pygame groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    # Initializing player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Initializing asteroid field. The object itself will spawn multiple asteroid objects
    asteroidfield = AsteroidField()

    # Game loop. 60 iterations per second (default). In each iteration, the game updates and redraws all the sprites
    while True:
        # Logger script. For development purposes
        log_state()
        
        # Kill the game on window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # In-game utility keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            print(player.__repr__())
        if keys[pygame.K_ESCAPE]:
            return
        
        # Paint the screen background in black
        screen.fill("black")
        
        # Updating updatable sprites
        updatable.update(dt)
        
        # Drawing drawable sprites
        for item in drawable:
            item.draw(screen)
        
        # Checking for asteroid collisions
        for asteroid in asteroids:
            # Collision with player
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            # Collision with shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    
        
        # Updating the surface object to the screen
        pygame.display.flip()
        
        # Setting delta time. Time between FPS (60 by default). clock.tick() gets the number of desired FPS as argument. 
        # Dividing by 1000 to get it in secons
        dt = clock.tick(MAX_FPS) / 1000

if __name__ == "__main__":
    main()
