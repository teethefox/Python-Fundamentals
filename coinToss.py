"""Assignment: Coin Tosses
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

Sample output should be like the following:

Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!
Hint: Use the python built-in round function to convert that floating point number into an integer"""
def coinToss():
  tosses=1
  heads=0
  tails=0
  while tosses <=5,000:
    import random
    chances = random.randrange(0,2)
    if chances >= 1:
      heads += 1
      print "Attempt #",tosses,":throwing a coin...It's heads...Got", heads,"heads so far and", tails, "tails so far"
    elif chances < 1:
      tails += 1 
      print "Attempt #",tosses,":throwing a coin...It's tails...Got", heads,"heads so far and", tails, "tails so far"
    tosses += 1 
coinToss()def coinToss():
  tosses=1
  heads=0
  tails=0
  while tosses <=10:
    import random
    chances = random.randrange(0,2)
    if chances >= 1:
      heads += 1
      print "Attempt #",tosses,":throwing a coin...It's heads...Got", heads,"heads so far and", tails, "tails so far"
    elif chances < 1:
      tails += 1 
      print "Attempt #",tosses,":throwing a coin...It's tails...Got", heads,"heads so far and", tails, "tails so far"
    tosses += 1 
coinToss()