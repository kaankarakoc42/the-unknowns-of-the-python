
class Person:
    age = 25
    name="kaan"
    
    @classmethod
    def printAge(self):
        print('The age is:', self.age)

    @staticmethod
    def printName(self):
        print('Name:', self.name)

#we dont need to create an object for use function printage because its a classmethod
Person.printAge()

#we should always give self argumant because its a staticmethod function
Person.printName(Person)
person=Person()
person.printName(person)