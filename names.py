"""students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
Michael Jordan
John Rosales
Mark Guillen
KB Tonel
"""
Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def order(list):
  print students[0]['first_name'], students[0]['last_name']
  print students[1]['first_name'], students[1]['last_name']
  print students[2]['first_name'], students[2]['last_name']
  print students[3]['first_name'], students[3]['last_name']

Part 2


def order(list):
  print "Students"
  print "1 - ",users["Students"][0]['first_name'], users["Students"][0]['last_name'], " - 13"
  print "2 - ",users["Students"][1]['first_name'], users["Students"][1]['last_name'], " - 11"
  print "3 - ",users["Students"][2]['first_name'], users["Students"][2]['last_name'], " - 11"
  print "4 - ",users["Students"][3]['first_name'], users["Students"][3]['last_name'], " - 4\n"
  print "Instructors"
  print "1 - ",users["Instructors"][0]['first_name'], users["Instructors"][0]['last_name'], " - 11"
  print "2 - ",users["Instructors"][1]['first_name'], users["Instructors"][1]['last_name'], " - 13"
  
order(users["Students"])