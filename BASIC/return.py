from typing import assert_type


def foo() -> int:
    return 1


assert_type(foo(), int)
assert_type(foo(), str)  # pyright: ignore
