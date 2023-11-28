class employee():
    # //Super class
 def __init__(self,name,age,salary):  
  self.name = name
  self.age = age
  self.salary = salary
class childemployee1(employee):
#   //First child class
 def __init__(self,name,age,salary):
  self.name = name
  self.age = age
  self.salary = salary
 
class childemployee2(childemployee1):
#   //Second child class
  def __init__(self, name, age, salary):
   self.name = name
   self.age = age
   self.salary = salary

class childemployee3(childemployee2):
#   //Second child class
  def __init__(self, name, age, salary):
   self.name = name
   self.age = age
   self.salary = salary   
emp1 = employee('harshit',22,1000)
emp2 = childemployee1('arjun',23,2000)
emp3 = childemployee3('ad')
 
print(emp1.age)
print(emp2.age)