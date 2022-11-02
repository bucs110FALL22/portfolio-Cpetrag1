import time
class Animal():
  def __init__(self, name = "", type = ""):
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d/%m/%y")
    self.adopted = None
    self.id = id(self)

  def set_adopted(self):
    self.adopted = time.strftime("%d/%m/%y")

  def manual_adopted(self, date = ""):
    self.adopted = date

  def __str__(self):
    str = f"The animal is a {self.type} and its name is {self.name}"
    str += f"\nAnimal id is : {self.id}"
    str += f"\nArival date: {self.arrived}"
    str += f"\nAdoption date: {self.adopted}"
    return str
 
def main():
  dan = Animal("Dan", "Dog")
  #Two different ways to set adoption date
  #dan.set_adopted()
  dan.manual_adopted("07/12/23")
  print(dan)
main()