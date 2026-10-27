from __future__ import annotations
T = dict((str, int) for _ in [()])
print('T:', T)
print('type of T:', type(T))
# This doesn't fire rule because it's not dict((k,v) for...) but dict((type, type)...)
# So expect_trigger=false. We show it's silent.
