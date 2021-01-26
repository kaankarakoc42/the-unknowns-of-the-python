class Person:
    def __init__(self):
        self._name="Kaan"
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,newName):
        Name=" ".join(["".join([n[0].upper(),n[1:]]) for n in newName.lower().split(" ")])
        self._name=Name
    
    @name.deleter
    def name(self):
        self._name="death"
        #del self._name

person=Person()
print(person.name)

person.name="steve jobs"
print(person.name)

del person.name
print(person.name)