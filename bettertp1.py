#text.split is cheating

question = input("you message:\n")
message = question + " "

def word_count(mes):
  word = None
  x = 0
  for i in mes:
      if i != " ":
          word = True
      elif i == " ":
          if word == True:
             x += 1
             word = False
  return x

print(word_count(mes = message))