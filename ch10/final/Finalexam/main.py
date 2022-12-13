import requests
import pygame
from Catpicture import Catpicture
from Catinfo import Catinfo
class Runner:
    def __init__(self):
      self.api1 = Catpicture()
      self.api2 = Catinfo()
    def execute(self):
      go = True
      while go:
        self.api1.getpic()
        print("")
        self.api2.getinfo()
        print("")
        decision = input("Do you want to see another picture or know another fact??(y/n)")
        if decision == 'n':
          go = False
final = Runner()
final.execute()
