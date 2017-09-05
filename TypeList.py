"""Assignment: Type List
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?"""
Type List 

def typeList(list):
  i = 0
  sum=0
  newstr=""
  while i < len(list):
    if type(list[i]) is str:
      newstr="".join(list[i])
    elif type(list[i]) is int:
      sum += list[i]
    i += 1
  if isinstance("list", (int, str)):
    print "The type of list was mixed, like me."
    print "The sum was",  sum, "if I can math right. Idk though."
    print "The string you enter was:",newstr, "'...super creative"