def gen():
    if TYPE_CHECKING:
        pass
    yield 1
    yield 2
it = gen()
print(next(it))
print(list(it))  # second consumption: should be [2] if gen() is lazy; if broken, may be [] or error
