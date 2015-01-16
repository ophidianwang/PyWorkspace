class Employee:
   'Common base class for all employees'
   empCount = 0   #static member

   def __init__(self, name, salary):
      #instance member
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
      "instance function: displayCount "
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      "instance function: displayEmployee "
      print "Name : ", self.name,  ", Salary: ", self.salary