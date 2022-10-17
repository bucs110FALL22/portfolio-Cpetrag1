def percentage_to_letter(score=0):
  if score >= 90:
    return 'A'
  elif 80 <= score < 90:
    return 'B'
  elif 70 <= score < 80:
    return 'C'
  elif 60 <= score < 70:
    return 'D'
  else:
    return 'F'
def is_passing(letter = None):
  if letter == 'A':
    return True
  elif letter == 'B':
    return True
  elif letter == 'C':
    return True
  else:
    return False
num = int(input("Input your score: "))
letter = percentage_to_letter(num)
print("Your letter grade is: " + letter)
print(is_passing(letter))