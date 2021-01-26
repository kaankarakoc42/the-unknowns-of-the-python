from dataclasses import dataclass

@dataclass
class DataClassCard:
    name: str
    job:  str
    age:  int #those classes only for data type description

example=DataClassCard("kaan","engineer",16)

print(f"name: {example.name}\njob: {example.job}\nage: {example.age}")

del example;print("-"*20)

example=DataClassCard("kaan","engineer","16")

print(f"name: {example.name}\njob: {example.job}\nage: {example.age}")