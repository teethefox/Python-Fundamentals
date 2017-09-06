"""
Write the following functions.

Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.

For example:"""

Part 1

def draw_stars(list):
  i = 0
  while i < len(list):
      stars= list[i]
      print "*"* stars
      i += 1

"""Part II
Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part."""
Part 2

def draw_stars(list):
  i = 0
  k=0
  while i < len(list):
    stars= list[i]
    if isinstance(stars, str):
      print (list[i][k])* len(list[i])
    else:
      print "*" * stars
    i += 1
