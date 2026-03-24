import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_radius = 1
        self.shot_cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        
    def update(self, dt):
        # Catch the pressed keys
        keys = pygame.key.get_pressed()
        
        # Reducing the shot cooldown
        self.shot_cooldown -= dt

        # Checking keys for player controls
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        # Only shoot in case the cooldown timer is set to 0
        if keys[pygame.K_SPACE] and not self.shot_cooldown > 0:
            self.shoot()
            self.shot_cooldown = PLAYER_SHOT_COOLDOWN_SECONDS
        
        # Added: When player ship reaches the edge of the screen, it pops up in the opposite edge   
        if self.position[0] <= 0:
            self.position = (SCREEN_WIDTH - 1, self.position[1])
        if self.position[0] >= SCREEN_WIDTH:
            self.position = (1, self.position[1])
        if self.position[1] <= 0:
            self.position = (self.position[0], SCREEN_HEIGHT - 1)
        if self.position[1] >= SCREEN_HEIGHT:
            self.position = (self.position[0], 1)
        
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector        
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def shoot(self):
        shot_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_vector = self.position + shot_vector * self.radius
        shot = Shot(shot_vector.x, shot_vector.y, self.shot_radius)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
    def __repr__(self):
        return f"Player position: {self.position}", f"Player rotation: {self.rotation}"