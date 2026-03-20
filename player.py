import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
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
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        
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
        
    def __repr__(self):
        return f"Player position: {self.position}", f"Player rotation: {self.rotation}"