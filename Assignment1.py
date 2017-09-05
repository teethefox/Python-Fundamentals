# Fucntion Find and Replace

def replace():
words = "It's thanksgiving day. It's my birthday,too!"
result = words.index("day")
print result
print words.replace("day","month")

# Function Max and Min
def maxmin(numbers):
  print max(numbers)
  print min(numbers)

#Function First and Last

def firstlast(list):
  list2 = [list[0] + list[len(list)-1]]
  print list2
firstlast(["happy", 344356, 43885, " meal"])

#Function New List

def newList(x):
  x.sort()
  list1 = x[:len(x)/2] 
  list2 = x[len(x)/2:]
  list2.insert(0,list1)
  print list2