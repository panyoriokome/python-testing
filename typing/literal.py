from typing import Literal, Set
from dataclasses import dataclass

@dataclass
class Error:
    error_code: Literal[1,2,3,4,5]
    disposed_of: bool

@dataclass
class Snack:
    name: Literal["Pretzel", "Hot Dog", "Veggie Burger"]
    condiments: Set[Literal["Mustard", "Ketchup"]]

# この3つはエラーになる
Snack("Pretzel", {"Mustard"}) 
Snack("Pretzel", {"Ketchup"})
Snack("Pretzel", {"Mustard", "Ketchup"})