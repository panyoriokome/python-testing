from typing import Literal, Set
from dataclasses import dataclass

# Vegetable = Literal['Tomato', 'Cucumber', 'Onion']
# lettuce: Vegetable = 'Lettuce'
# print(lettuce)

@dataclass
class ToDo:
    title: str
    status: Literal['ToDo', 'Doing', 'Done']

todo1 = ToDo('牛乳を買う', 'ToDo')
print(todo1.status)


todo2 = ToDo('牛乳を買う', 'Ready')
print(todo2.status)
print(todo2)