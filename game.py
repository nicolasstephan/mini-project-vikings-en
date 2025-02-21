# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("⚔️🔥 WarGame")
running = True
dt = 0

# Load the image
image = pygame.image.load("your_image.png")

# Resize the image (optional, to fit the screen)
image = pygame.transform.scale(image, (width, height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the image onto the screen
    screen.blit(image, (0, 0))

    keys = pygame.key.get_pressed()
   #go ot next round

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()


