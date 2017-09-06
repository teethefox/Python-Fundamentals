"""Assignment: Dictionary in, tuples out
Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:"""
"""Assignment: Dictionary in, tuples out
Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:"""
dic =  {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
  }
def tuplesOut(obj):
  tuple=()
  for key, value in dic.iteritems() :
   tuple +=   key, value
   
  print (tuple[0],tuple[1]),",",(tuple[2], tuple[3]),",",(tuple[4],tuple[5])
tuplesOut(dic)
   
   