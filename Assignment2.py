"""Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000."""
Multiples
#prints odds from 1-1,000
for count in range(1,1000):
  if count % 2 != 0:
    print count
    count += 1

#prints multiples of 5 from 5-1,000,000
for count in range(5,1000000):
  if count % 5 == 0:
    print count
    count+=1
"""Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]"""
Sum List

a = [1, 2, 5, 10, 255, 3]
i = 0
sum=0
while i < len(a):
    sum+=(a[i])
    i += 1
print sum

"""Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]"""
Sum List

a = [1, 2, 5, 10, 255, 3]
i = 0
sum=0
while i < len(a):
    sum+=(a[i])
    i += 1
    avg = sum / len(a)
print avg
    
    