"""Assignment: Fun with Functions
Create a series of functions based on the below descriptions.

Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

Your program output should look like below:"""
Odd/Even


def odd_even():
  for i in range(1,2000):
    if i % 2 == 1:
      print i, ": odd"
    elif i % 2 != 1:
      print i, ":even"
odd_even()

"""Multiply

Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. For example, let's say:"""
Multiply 


def multiply(list, num):
  i=0 
  newList= []
  while i < len(list):
    newList.append(list[i]*num)
    i += 1
  print newList
  """Hacker Challenge:
Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's an example:"""

Hacker Challenge


"""Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. For example, let's say:
  Hacker Challenge:
Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's an example:"""

#Code changed for second challenge
 
def multiply(list, num):
    for x in range(0, len(list)):
        list[x] *= num
    return list

numbers_array = [3, 6, 8, 10, 67]

print multiply(numbers_array, 5)

def layered_multiples(list):
    print list
    new = []
    for x in list:
        val = []
        for i in range(0,x):
            val.append(1)
        new.append(val)
    return new

x = layered_multiples(multiply([2,4,5],3))
print x