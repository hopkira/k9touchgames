import pygame

pygame.init()

width  = 1024
height = 786

size = (width,  height)

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Anagram Game")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

def draw_word(word:str, size:int, line:int) -> list:
    rects = []
    letterfont = pygame.font.SysFont('Corbel',size)
    for num,letter in enumerate(word):
        text = letterfont.render(letter,True,WHITE)
        text_rect = text.get_rect(center = (width/2 + ((num-2.5) * (size * 1.1)), line * size * 1.1))
        # pygame.draw.rect(screen, RED, text_rect, 0)
        rect  = (((width/2) -size/2 + ((num-2.5) * size * 1.1)), -size/2 + line * size * 1.1, size, size)
        pygame.draw.rect(screen, WHITE, rect, width=3, border_radius=7)
        rect = tuple(letter) + rect
        rects.append(rect)
        screen.blit(text, text_rect)
    return rects

touch_spots = []
touch_spots = touch_spots + draw_word("WORDLE", 150, 1)
touch_spots  = touch_spots + draw_word("INPUT_", 150, 2)
# -------- Main Program Loop -----------

while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we can exit the while loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                print(touch_spots)
                pygame.quit()
 
     # --- Game logic should go here
    mouse = pygame.mouse.get_pos()
     # --- Drawing code should go here
     # First, clear the screen to white. 
    screen.fill((60,25,60))
    #The you can draw different shapes and lines or add text to your background stage.
    #pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
    #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
    draw_word("WORDLE", 150, 1)
    draw_word("INPUT_", 150, 2)

    # --- Go ahead and update the screen with what we've drawn.
    #pygame.display.flip(
    pygame.display.update()
     
     # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
print(touch_spots)
pygame.quit()
