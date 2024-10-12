"""
Create a new type called Vector, which is a list of float.
"""

from typing import List

Vector = List[float]


## End of your code ##
def foo(v: Vector): ...


foo([1.1, 2])
foo(1)  # pyright: ignore
foo(["1"])  # pyright: ignore
