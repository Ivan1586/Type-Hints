def foo(x: tuple[str, int]):
    pass


foo(("foo", 1))

foo((1, 2))  # pyright: ignore
foo(("foo", "bar"))  # pyright: ignore
foo((1, "foo"))  # pyright: ignore
