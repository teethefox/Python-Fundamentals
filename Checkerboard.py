"""Assignment: Checkerboard
Write a program that prints a 'checkerboard' pattern to the console.

Your program should require no input and produce console output that looks like so:"""
one=" "
two="*"
i=0
while i < 200:
  if i % 2 == 1:
    print one + two + one + two + one + two + one
  elif i % 2 != 1:
    print two + one + two + one + two + one
  i += 1
  