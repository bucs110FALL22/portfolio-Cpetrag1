class Player:
  def player(self):
    self.is_fast = False
    self.lives = 5
    self.id = 1
class Mushroom:
  def mushroom(self):
    self.hits_to_kill = 2
    self.alive = True
    self.is_large = False
class Block:
  def block(self, x, y):
    self.is_hit = False
    self.inside = "1 coin"
    self.pos = (x,y)
    