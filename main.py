import os

program = input("Which part? (A, B, C, D) ").lower()

while program not in ["a", "b", "c", "d"]:
  os.system('clear')
  print("Not a valid input.")
  program = input("Which part? (A, B, C, D) ").lower()

if program == 'a':
  import Aquicklineplot

elif program == 'b':
  import Blineplots

elif program == 'c':
  import Cbargraphs

elif program == 'd':
  import Dscatterplot1