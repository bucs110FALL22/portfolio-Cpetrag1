class StringUtility:
  def __init__(self,string = ""):
    self.string = string
  def __str__(self):
    return self.string
  def vowels(self):
    vow = 0
    for i in self.string:
      if i == 'A':
        vow = vow +  1
      if i == 'E':
        vow = vow + 1
      if i == 'I':
        vow = vow + 1
      if i == 'O':
        vow = vow + 1
      if i == 'U':
        vow = vow + 1
      if i == 'a':
        vow = vow + 1
      if i == 'e':
        vow = vow + 1
      if i == 'i':
        vow = vow + 1
      if i == 'o':
        vow = vow + 1
      if i == 'u':
        vow = vow + 1
    if vow >= 5:
      return "too many"
    return vow
  def bothends(self):
    if len(self.stirng) <= 2:
      return ""
    str = f"{self.string[0]} + {self.string[1]} + {self.string[-2]} + {self.string[-1]}"
    return str
    
    