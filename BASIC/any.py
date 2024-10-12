"""
Modify `foo` so it takes an argument of arbitrary type.
"""

from typing import Union


def foo(data_1: Union[str, int]):
    """⬆️ Change me. No need to implement the function."""


foo(1)
foo("10")
foo(1, 2)  # pyright: ignore
