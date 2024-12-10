import json

class Employee:
    def __init__(self, id: int, name: str, salary: float) -> None:
        self._id = id
        self._name = name
        self._salary = salary

    def __str__(self) -> str:
        return f"{self._id}, {self._name}, {self._salary}"
    
    def appraisal(self, percent):
        self._salary += self._salary * percent/100
    


## JSON OPERATIONS ############################################################

def JSONStorage(fileName):
    # 1. Create Employee object
    emp = Employee(111, "Rakesh", 100000)

    # 2. Convert to a dictionary
    dt = {"id": emp._id,
        "name": emp._name,
        "salary": emp._salary
        }

    # 3. Save to a file
    with open(fileName, 'w') as file:
        json.dump(dt, file)

def JSONModifyFile(fileName):
    # 4. Read from file to dictionary
    with open(fileName, 'r') as file:
        dt = json.load(file)
    print(dt)

    # 5. Convert to object
    obj = Employee(dt['id'], dt['name'], dt['salary'])
    print(obj)

    # 6. Modify the object
    obj.appraisal(10)
    print(obj)

    # 7. Convert to a dictionary
    dt = {"id": obj._id,
        "name": obj._name,
        "salary": obj._salary
        }
    print(dt)
    
    # 8. Save to a file
    with open(fileName, 'w') as file:
        json.dump(dt, file)


def JSONOperations():
    JSONStorage('Employee.json')
    JSONModifyFile('Employee.json')



## Pickle Operations ##########################################################

import pickle

def PickleStorage(fileName):
    # 1. Create Employee object
    emp = Employee(111, "Rakesh", 100000)

    # 2. Save object to a file
    with open(fileName, "wb") as file:
        pickle.dump(emp, file)

def PickleModifyFile(fileName):
    # 3. Read from file to object
    with open(fileName, 'rb') as file:
        obj = pickle.load(file)
    print(obj)

    # 4. Modify the object
    obj.appraisal(10)
    print(obj)

    # 5. Save object to a file
    with open(fileName, 'wb') as file:
        pickle.dump(obj, file)


def PickleOperations():
    PickleStorage('Employee.pkl')
    PickleModifyFile('Employee.pkl')


if __name__ == '__main__':
    print("Testing JSON")
    JSONOperations()

    print("="*40)

    print("Testing Pickle")
    PickleOperations()