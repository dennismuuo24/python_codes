import pygame;
pygame.init();
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sliding Puzzle")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Define the puzzle board size
rows = 3
cols = 3

# Define the size of each puzzle piece
piece_width = screen_width // cols
piece_height = screen_height // rows

# Draw the puzzle pieces
for row in range(rows):
    for col in range(cols):
        piece_x = col * piece_width
        piece_y = row * piece_height
        pygame.draw.rect(screen, (255, 255, 255), (piece_x, piece_y, piece_width, piece_height))
        pygame.display.update()
        pygame.quit()