import pygame
import sys
import asyncio

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Ball")

async def main():

    # Colors
    WHITE = (255, 255, 255)
    BLUE = (50, 100, 255)

    # Ball properties
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_radius = 25
    speed = 5

    # Clock for frame rate
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    while running:

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key presses
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            ball_x -= speed
        if keys[pygame.K_RIGHT]:
            ball_x += speed
        if keys[pygame.K_UP]:
            ball_y -= speed
        if keys[pygame.K_DOWN]:
            ball_y += speed

        # Keep the ball on the screen
        ball_x = max(ball_radius, min(ball_x, WIDTH - ball_radius))
        ball_y = max(ball_radius, min(ball_y, HEIGHT - ball_radius))

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

        # Update display
        pygame.display.flip()

        # Limit to 60 FPS
        clock.tick(60)
        
        asyncio.sleep(0)

        # Quit cleanly
        pygame.quit()
        sys.exit()

    asyncio.run(main())