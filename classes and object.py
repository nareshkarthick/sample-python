class person:
    #class attribute
    name = " "
    age = 0
    height = " "
    weight = " "

#creating person1 object

person1 = person()
person1.name = 'anand'
person1.age = 23
person1.height = '6 ft'
person1.weight = '60kg'

#creating person2 object
person2 = person()
person2.name = 'yogesh'
person2.age = 22
person2.height = '5.5 ft'
person2.weight = '67kg'

#creating person3 object
person3 = person()
person3.name = 'naresh'
person3.age = 23
person3.height = '5 ft'
person3.weight = '65kg'

print(f'{person1.name} is {person1.age} years old, height is {person1.height} and weight is {person1.weight}')
print(f'{person2.name} is {person2.age} years old, height is {person2.height} and weight is {person2.weight}')
print(f'{person3.name} is {person3.age} years old, height is {person3.height} and weight is {person3.weight}')
