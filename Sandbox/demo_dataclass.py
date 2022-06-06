from dataclasses import dataclass

# A basic Data Class
@dataclass
class employee:
    # Attributes Declaration
    # using Type Hints
    emp_id: str
    name: str
    age: int
    city: str

emp1 = employee("Peter", "peter858", 45, 'Lhee')
emp2 = employee("Guido", "guido23", 28, 'Utrecht')
emp3 = employee("Albert", "albert58", 34, 'Amsterdam')
emp4 = employee("Albert", "albert58", 34, 'Amsterdam')

print("employee objects are :")
print(emp1)
print(emp2)
print(emp3)
print(emp4)

print()

# referring two object to check equality
print("Data in emp1 and emp2 are same? ", emp1 == emp2)
print("Data in emp1 and emp3 are same? ", emp1 == emp3)
print("Data in emp1 and emp3 are same? ", emp3 == emp4)
