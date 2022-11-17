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
YELLOW  = (255,255,0)

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


class Letter():
    '''
    Refactored letter class
    '''
    def __init__(self, letter:str, size:int, row:int, col:int, colour: tuple)  -> tuple:
        self.letter = letter
        self.size = size
        self.row = row
        self.col = col
        self.colour = colour
        self.rect  = (int((width/2) -size/2 + ((col-2.5) * size * 1.1)), int(-size/2 + row * size * 1.1), size, size)

    def draw(self, colour: tuple):
        letterfont = pygame.font.SysFont('Corbel',size)
        text = letterfont.render(self.letter,True, colour)
        text_rect = text.get_rect(center = (width/2 + ((self.col-2.5) * (self.size * 1.1)), self.row * self.size * 1.1))
        pygame.draw.rect(screen, colour, self.rect, width = 5, border_radius = 7)
        screen.blit(text, text_rect)

    def is_touched(self) -> bool:
        left,top,box_width,box_height = self.rect
        if left <= mouse[0] <= left + box_width and top <= mouse[1] <= top + box_height:
            self.draw(colour = GREEN)
            return True
        else:
            self.draw(colour = self.colour)
            return False


class Word():
    '''
    Refactored word class
    '''
    def __init__(self,word:str,size:int, row:int,col:int, colour:tuple):
        self.word = word
        self.size = size
        self.row = row
        self.col = col
        self.colour = colour

    def draw(self) -> list:
        word_list = []
        for col,letter in enumerate(list(self.word)):
            new_letter = Letter(letter, self.size, self.row, self.col + col, self.colour)
            new_letter.draw(self.colour)
            word_list.append(new_letter)
        return word_list


class Timer():
    '''
    Timer
    '''
    def __init__(self):
        self.timer = 1000
        self.timer_size = size * 6 * 1.1
        self.colour = GREEN

    def draw(self):
        time = self.timer / 1000
        if time < 0.333:
            self.colour = RED
        if time  >= 0.333 and time <= 0.666:
            self.colour = YELLOW
        if time > 0.666:
            self.colour = GREEN
        pygame.draw.rect(screen, DARK_GREEN, [int((width/2)-3*(size*1.1)), int((5*size)), int(self.timer_size), 80], width = 5, border_radius = 7)
        pygame.draw.rect(screen, BLACK, [int(width/2)-((3*(size*1.1))-20), int(5*size+20), int(self.timer_size-40), 40], border_radius = 7)
        pygame.draw.rect(screen, self.colour, [int((width/2)-(time*(3*(size*1.1))-20)), int(5*size+20), int((self.timer_size-40) * time), 40], border_radius = 7)
    
    def timer_expired(self, amount:int = 1) -> bool:
        self.timer = self.timer - amount
        if self.timer > 0:
            return False
        else:
            return True

    def reset_timer(self):
        self.timer = 100


# Draw board 
screen.fill(BLACK)

score_line = Word("000000",150,1,0,BR_GREEN)
anagram_line = Word("      ", 150, 2, 0, DARK_GREEN)
input_line = Word("MASTER", 150, 3, 0, GREEN)
lives_line = Word("LIVES3", 150, 4, 0, DARK_GREEN)
lines  = []

score_word = score_line.draw()
anagram_word = anagram_line.draw()
input_word = input_line.draw()
livess_word = lives_line.draw()

timer = Timer()

# -------- Main Program Loop -----------
time = 1
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we can exit the while loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            for letter in input_word:
                if letter.is_touched():
                    letter.draw(YELLOW)
                    print(letter.letter)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                carryOn = False

     # --- Game logic should go here
    mouse = pygame.mouse.get_pos()
     # --- Drawing code should go here

    timer.draw()
    if timer.timer_expired():
        carryOn = False
    
    clock.tick(50)
    pygame.display.update()
# -------- End of Main Program Loop

pygame.quit()
