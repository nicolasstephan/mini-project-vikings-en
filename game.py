import pygame
import wargame
import random

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("⚔️🔥Vikings VS Saxons⚔️🔥")
clock = pygame.time.Clock()
running = True
dt = 0  # Delta time for smooth movement

# Load background
background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (1280, 720))

# Button settings
button_color = "black"
button_width, button_height = 200, 100
button_x = (screen.get_width() - button_width) // 2 
button_y = (screen.get_height() - button_height) // 2
button_rect = pygame.Rect(button_x, button_y, button_width, button_height) 


# Player (Temporary Red Circle)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

soldiers_images = ["Viking1.png","Viking2.png","Viking3.png","Viking4.png","Viking5.png","Saxon1.png","Saxon2.png","Saxon3.png","Saxon4.png","Saxon5.png"]



# Viking Sprite Class
class Soldiers(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image_path = random.choice(soldiers_images) 
        self.image = pygame.image.load(image_path).convert_alpha() 
        self.image = pygame.transform.scale(self.image, (90, 90)) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Create a Sprite Group for Multiple Vikings
soldier_group = pygame.sprite.Group()

# Generate 5 Vikings with Random Images and Positions
for _ in range(10):
    x = random.randint(50, 1200) 
    y = random.randint(150, 550)  
    soldier = Soldiers(x, y)
    soldier_group.add(soldier) 

# Game Loop
while running:

    # Draw Background First
    screen.blit(background, (0, 0))

    # Draw All Viking Sprites
    soldier_group.draw(screen)

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, button_color, button_rect)

     # Button text
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Fight!", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    # Message display settings
    message = ""
    font = pygame.font.Font(None, 36)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(mouse_pos):
            wargame.main()  # Call the main function of wargame.py

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Refresh Screen
    pygame.display.flip()

    # Delta Time
    dt = clock.tick(60) / 1000

pygame.quit()
