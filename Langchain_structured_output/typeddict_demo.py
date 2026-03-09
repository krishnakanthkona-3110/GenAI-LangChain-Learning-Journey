from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'krish', 'age':28}

print(new_person)
