def get_list() -> list[int]:
    return [42]
annotated: int = get_list()[0]  # Not a trigger; need list()
first = int(list(get_list())[0])  # RUF015 trigger
print(f'first:{first}')
