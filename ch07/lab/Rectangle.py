class Rectangle:
  def __init__(self, x=0, y=0, h=0, w=0):
    if x<0:
      x=0
    if y < 0:
      y = 0
    if h<0:
      h = 0
    if w<0:
      w = 0
    self.x = x
    self.y = y
    self.height = h
    self.width = w
  def __str__(self):
    return (f"(x: , {self.x},y: {self.y}, width: {self.width}, height: {self.height}")