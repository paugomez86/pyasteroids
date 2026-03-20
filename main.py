import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
    
    # Adding classes to pygame groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    # Initializing player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Initializing asteroid field. The object itself will spawn multiple asteroid objects
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            print(player.__repr__())
        if keys[pygame.K_ESCAPE]:
            return
                
        screen.fill("black")
        
        updatable.update(dt)
        
        for item in drawable:
            item.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(MAX_FPS) / 1000

if __name__ == "__main__":
    main()
