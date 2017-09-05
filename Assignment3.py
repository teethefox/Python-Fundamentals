"""Assignment: Filter by Type
Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

Integer
If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

String
If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

List
If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

Test your program using these examples:"""

def myType(input):
  if type(input) is int:
    if input >= 100:
      print "Chill with that big number, yo!"
    elif input <100:
      print "Aye, that's a lil' small"
  elif type(input) is str:
    if len(input)>= 50:
      print "You kinda talk too much"
    elif len(input) < 50:
      print "You mumblin' or somethin'"
  elif type(input) is list:
    if len(input)>= 10:
      print "Daaaaaannnnngg okay with that big ol' list. I see you boo."
    elif len(input)<10:
      print "Uhhhh, you gonna give me a real list or not?"
