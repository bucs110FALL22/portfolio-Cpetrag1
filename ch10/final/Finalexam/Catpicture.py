import requests
import pygame
from io import BytesIO
class Catpicture:
  
  def __init__(self):
    self.api_url = "https://cataas.com/cat"
    
  def getpic(self):
    cat = requests.get(self.api_url)
    image_data = BytesIO(cat.content)
    image = pygame.image.load(image_data)
    width, height = image.get_size()
    display = pygame.display.set_mode((width, height))
    display.blit(image, (0, 0))
    pygame.display.update()
    
    

