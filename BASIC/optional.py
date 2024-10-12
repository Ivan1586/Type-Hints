def foo(x: int | None = 0):
    pass


foo(10)
foo(None)
foo()

foo("10")  # pyright: ignore
