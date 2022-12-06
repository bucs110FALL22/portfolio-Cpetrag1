import pygame
import sys
from random import randint


# Variables for screen size and border width
screen_size = 640
singleblock_size = screen_size // 3

# variable to create grid
notfilled = float('inf')
vec2 = pygame.math.Vector2

# sets top left caption to game name
pygame.display.set_caption('Tic Tac Toe')

# main runner class and method
class Runner:
  def __init__(self, board):
    self.board = board
    # creates font used in tie screen
    self.font = pygame.font.SysFont('Arial', singleblock_size // 8, True)

    # putting images from markers folder into variables
    self.bg_image = self.imagefitting(path = 'markers/TTTboard.png', res = [screen_size]*2)
    self.ximg = self.imagefitting(path = 'markers/X.png', res = [singleblock_size] * 2)
    self.oimg = self.imagefitting(path = 'markers/O.png', res = [singleblock_size] * 2)
    self.xwins_img = self.imagefitting(path = 'markers/Xwins.png', res = (640,640))
    self.owins_img = self.imagefitting(path = 'markers/Owins.png', res = (640,640))

    # Represents empty cells in an array
    self.grid = [[notfilled, notfilled, notfilled],
                [notfilled, notfilled, notfilled],
                [notfilled, notfilled, notfilled]]
    self.playerturn = randint(0,1)
    # All possible wins in tic tac toe
    self.possible_win_aaray = [[(0,0), (0,1), (0,2)],
                         [(1,0), (1,1), (1,2)],
                         [(2,0), (2,1), (2,2)],
                         [(0,0), (1,0), (2,0)],
                         [(0,1), (1,1), (2,1)],
                         [(0,2), (1,2), (2,2)],
                         [(0,0), (1,1), (2,2)],
                         [(0,2), (1,1), (2,0)]]
    self.winner = None
    self.num_turns = 0
    
  
  # Scales image to board
  @staticmethod
  def imagefitting(path, res):
    img = pygame.image.load(path)
    return pygame.transform.smoothscale(img, res)

  # if grid space is not equal to notfilled we display X and O
  def draw_objects(self):
    for y, row in enumerate(self.grid):
      for x, obj in enumerate(row):
        if obj != notfilled:
          self.board.screen.blit(self.ximg if obj else self.oimg, vec2(x,y) * singleblock_size)

  # Checks if the cell clicked is already used and if not fills the box and adds 1 to the number of turns played
  def run_game(self):
    cur_block = vec2(pygame.mouse.get_pos()) // singleblock_size
    column, row = map(int, cur_block)
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and self.grid[row][column] == notfilled and not self.winner:
      self.grid[row][column] = self.playerturn
      self.playerturn = not self.playerturn
      self.num_turns += 1
      self.checkwinner()

  # draws the tic tac toe board
  def draw_board(self):
    self.board.screen.blit(self.bg_image, (0,0))
    self.draw_objects()
    self.display_winner()

  # Displays whose turn it is in the top left corner
  def caption_turn(self):
    pygame.display.set_caption(f'Player "{"OX"[self.playerturn]}" turn')

  # Checks possible win array for a winner
  def checkwinner(self):
    for line in self.possible_win_aaray:
      sum_line = sum([self.grid[i][j] for i, j in line])
      if sum_line in {0,3}:
        self.winner = 'XO'[sum_line == 0]

  # Displays the winner with images from the markers folder and also displays tie
  def display_winner(self):
    if self.winner == 'X':
      self.board.screen.blit(self.xwins_img, (0,0))
    elif self.winner == 'O':
      self.board.screen.blit(self.owins_img, (0,0))
    elif self.num_turns == 9:
      statement1 = self.font.render("There is a Tie. Press the space" ,True, "red", "green")
      statement2 = self.font.render("bar to play again", True, "red", "green")
      
      self.board.screen.blit(statement1, (100, 100))
      self.board.screen.blit(statement2, (100, 135))
      
  # Runs game   
  def run(self):
    self.caption_turn()
    self.draw_board()
    self.run_game()

# Board class where events will be checked and game will be run
class Board:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode([screen_size]*2)
    self.clock = pygame.time.Clock()
    self.runner = Runner(self)

  # Checks to see if user has exited the application and checks for the user restarting the game
  def check_events(self):
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if i.type == pygame.KEYDOWN:
        if i.key == pygame.K_SPACE:
          self.restart()

  # if spacebar is pressed this function restarts the game
  def restart(self):
    self.runner = Runner(self)

  # Used to check events while game is going on
  def play(self):
    playing = True
    while playing:
      self.runner.run()
      self.check_events()
      pygame.display.update()
      self.clock.tick(60)

if __name__ == '__main__':
  board = Board()
  board.play()
