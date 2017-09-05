"""Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:"""

Compare lists

def compare(list1, list2):
  if list1 == list2:
     print "identical twins, congrats"
  else:
    print "Not a match"