import requests
class Catinfo:
    def __init__(self):
      self.api_url = 'https://meowfacts.herokuapp.com/'

    def getinfo(self):
      info = requests.get(self.api_url)
      cat = info.json()
      print("Check the output to see a picture of a cat!\n")
      print("Heres a random cat fact to go along with your cat!!: \n")
      print(str(cat['data']))
        
