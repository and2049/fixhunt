def f() -> Generator[int, None, None]:
    try:
        raise ValueError('test')
    except ValueError as e:
        yield 1
    else:
        yield 2
    finally:
        yield 3
gen = f()
print(list(gen))
