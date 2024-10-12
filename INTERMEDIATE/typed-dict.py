"""
Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string
"""

from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: str


a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
a: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  # pyright: ignore
a: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  # pyright: ignore
a: Student = {
    "name": "Tom",
    "age": "2",  # pyright: ignore
    "school": "Hogwarts",
}
a: Student = {"name": "Tom", "age": 2}  # pyright: ignore
assert Student(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)
