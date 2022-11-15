import pygame

pygame.init()

size = 150

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
DARK_GREEN = ( 0, 132, 74)
BR_GREEN = (0, 66, 37)
RED = ( 255, 0, 0)

# light shade of the button
colour_light = (170,170,170)
  
# dark shade of the button
colour_dark = (100,100,100)

#screen = pygame.display.set_mode(win_size)
#screen = pygame.display.set_mode((win_size), pygame.FULLSCREEN)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

info = pygame.display.Info()
win_size = width, height = info.current_w, info.current_h

pygame.display.set_caption("Anagram Game")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

def draw_letter(letter:str, size:int, row:int, col:int, colour:tuple) -> list:
    letterfont = pygame.font.SysFont('Corbel',size)
    # for num,letter in enumerate(word):
    text = letterfont.render(letter,True,DARK_GREEN)
    text_rect = text.get_rect(center = (width/2 + ((col-2.5) * (size * 1.1)), row * size * 1.1))
    # pygame.draw.rect(screen, RED, text_rect, 0)
    rect  = (int((width/2) -size/2 + ((col-2.5) * size * 1.1)), int(-size/2 + row * size * 1.1), size, size)
    pygame.draw.rect(screen, colour, rect, width=5, border_radius=7)
    rect = tuple(letter) + rect
    screen.blit(text, text_rect)
    return rect

def draw_word(word:str,size:int, row:int,col:int, colour:tuple) -> list:
    rects = []
    start_col = col
    for col,letter in enumerate(list(word)):
        rect = draw_letter(letter, size, row, col + start_col, colour)
        rects.append(rect)
    return rects

def touch_spot(touch_spots) -> str:
    for num,spots in enumerate(touch_spots):
        letter,left,top,box_width,box_height = touch_spots[num]
        if left <= mouse[0] <= left + box_width and top <= mouse[1] <= top + box_height:
            pygame.draw.rect(screen,DARK_GREEN,[left, top, box_width, box_height], width=5,border_radius=7)
            letterfont = pygame.font.SysFont('Corbel',int(size))
            # for num,letter in enumerate(word):
            text = letterfont.render(letter,True,GREEN)
            text_rect = text.get_rect(center = ( left + box_width/2, top + box_height/2  ))
            screen.blit(text, text_rect)
            return letter

touch_spots = []
touch_spots = touch_spots + draw_word("WORDLE", 150, 2, 0, colour_dark)
touch_spots = touch_spots + draw_word("INPUT_", 150, 3, 0, colour_dark)
touch_spots = touch_spots + draw_word("PASS", 150, 4, 1, RED)

# -------- Main Program Loop -----------

while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we can exit the while loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(touch_spot(touch_spots))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                carryOn = False

     # --- Game logic should go here
    mouse = pygame.mouse.get_pos()
     # --- Drawing code should go here
     # First, clear the screen to white. 
    screen.fill(BLACK)
    #The you can draw different shapes and lines or add text to your background stage.
    #pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
    #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
    #if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
    #    pygame.draw.rect(screen,colour_light,[width/2,height/2,140,40])
    #else:
    #    pygame.draw.rect(screen,colour_dark,[width/2,height/2,140,40])
    draw_word("WORDLE", 150, 2, 0, BR_GREEN)
    draw_word("INPUT_", 150, 3, 0, BR_GREEN)
    draw_word("PASS", 150, 4, 1, RED)

    touch_spot(touch_spots)
    # --- Go ahead and update the screen with what we've drawn.
    #pygame.display.flip(
    pygame.display.update()
     
     # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
# print(touch_spots)
pygame.quit()
