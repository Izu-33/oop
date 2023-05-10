# Object-Oriented Programming

Writing clean code is a key component of OOP.

OOP is centered around classes and objects.

## Sample Code

```
class Employee:
    def __init__(self, nom, age, sal, position, department, marital_status):
        self.name = nom
        self.age = age
        self.salary = sal
        self.position = position
        self.department = department
        self.marital_status = marital_status
        
    def add_age(self):
        self.age += 1
        
    def get_age(self):
        return "Age is {}".format(self.age)
```

## Pillars of OOP

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction


