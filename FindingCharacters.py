"""Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character."""
def findCharacters(list, str):
  i = 0
  newstr=[]
  while i <len(list):
    j = 0
    while j < len(list[i]):
        if list[i][j] == str:
          newstr.append(list[i])
        j += 1
      
    i += 1
  print newstr