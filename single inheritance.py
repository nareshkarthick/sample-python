class employee():
    # //This is a parent class
 def __init__(self, name, age, salary):  
  self.name = name
  self.age = age
  self.salary = salary
 
class childemployee1(employee):
#   //This is a child class
 def __init__(self, name, age, salary,id):
  self.name = name
  self.age = age
  self.salary = salary
  self.id = id
emp1 = employee('harshit',22,1000)

print(emp1.name)
print(emp1.age)
print(emp1.salary)
 
class childemployee2(employee):
#   //This is a child class
 def __init__(self, name, age, salary, id):
  self.name = name
  self.age = age
  self.salary = salary
  self.id = id
emp2 = employee('krish',23,2000)
print(emp2.name)
print(emp2.age)
print(emp2.salary)

