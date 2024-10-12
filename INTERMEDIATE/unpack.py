"""
`foo` expects two keyword arguments - `name` of type `str`, and `age` of type `int`.
"""

from typing import TypedDict, Unpack


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]): ...


person: Person = {"name": "The Meaning of Life", "age": 1983}
foo(**person)
foo(**{"name": "Brian", "age": 30})

foo(**{"name": "Brian"})  # pyright: ignore
person2: dict[str, object] = {"name": "Brian", "age": 20}
foo(**person2)  # pyright: ignore
foo(**{"name": "Brian", "age": "1979"})  # pyright: ignore
