import contextlib


@contextlib.contextmanager
def test_context(name):
    print(f"enter,my name {name}")

    yield

    print(f"exit ,my name {name}")


with test_context("aaa"):
    pass
