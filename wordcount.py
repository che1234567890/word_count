message = input("you message:\n")


def word_count(mes):
  x = 0
  for i in mes:
    x += 1 
  print(x)

word_count(mes = message)
