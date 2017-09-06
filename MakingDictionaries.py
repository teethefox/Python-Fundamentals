"""Assignment: Making Dictionaries
Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.

Your first function will take in two lists containing some strings. Here are two example lists:"""
Part 1 & 2
list1 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "piano"]
list2 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "clavicle"]
def making(list1,list2):
  newDic = {}
  i = 0
  if len(list1) >= len(list2):
    key= list1 
    value = list2
  else:
    key= list2 
    value= list2
  while i <= key:
    newDic = {key[i]: value[i]}
    print newDic
    i += 1
making(list1,list2)