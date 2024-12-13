from dataclasses import dataclass, field
from typing import List

@dataclass#(frozen=True)
class Person:
    id: int = field(repr=False)
    name: str
    city: str
    age: int = field(default=0)#, repr=False)
    active: bool = True

    def __post_init__(self):
        self.age += 10
        
@dataclass
class Office:
    employees: List[str] = field(default_factory=list)






p1 = Person(id=1, name="Vinayak", city="Bangalore", age = 20, active=False)
print(p1)
print(repr(p1))

p2 = Person(id=2, name="Vinay", city="Chennai")
print(p2)

print(p1 == p2)
# print(p1 < p2)
# print(p1 > p2)


site = Office()
site.employees.append("Bob")
