import abc

records = []

@staticmethod
@abc.abstractmethod
def make_counter():
    n = 0
    def counter():
        nonlocal n
        n += 1
        records.append(('call', n))
        return n
    return counter

# Rewrite should become @staticmethod\n@abc.abstractmethod
counter_func = make_counter()

class CounterBase(abc.ABC):
    pass
CounterBase.get_count = counter_func

# Use walrus in comprehension
results = [x for y in range(3) if (x := CounterBase().get_count()) > 0]

# Late-binding lambda hazard
funcs = []
for i in range(2):
    funcs.append(lambda: CounterBase().get_count() + i)

try:
    f1, f2 = funcs
    late = f1()  # should be 1 + 0 = 1 if i captured, else 1+1=2
    records.append(('late', late))
except Exception as e:
    records.append(('error', str(e)))

print(','.join(map(str, records)))
