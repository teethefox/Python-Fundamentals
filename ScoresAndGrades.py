"""Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A"""
Scores And Grades

i= 0 
while i < 10:
  import random
  score= random.randint(60, 100)
  if score >= 60 and score < 70:
    grade= "D"
  elif score >=70 and score < 80:
    grade="C"
  elif score >=80 and score <90:
    grade="B"
  elif score>=90 and score <=100:
    grade="A"
  print "Score:", score, "Grade:", grade
  i +=1
print "That's all , folks."