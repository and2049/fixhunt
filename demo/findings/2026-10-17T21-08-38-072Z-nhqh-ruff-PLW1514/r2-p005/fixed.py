import os

with open('test.txt', 'w') as f:
    f.write('hi')

kwargs = {'encoding': 'utf-8'}
try:
    # Rule fires on open('test.txt') and adds encoding='utf-8'
    # But **kwargs also has encoding -> duplicate
    f = open('test.txt', **kwargs)  # This line is NOT touched by rule
    print('Read:', f.read())
    f.close()
except TypeError as e:
    print('TypeError:', e)

# Now make the rule trigger on a call WITHOUT **kwargs but we simulate hazard via comment
# Actually, to trigger rule AND have **kwargs with encoding, we need:
# But rule only adds if no encoding present. So we need a call like open(x) + **{'encoding':x}
# That would be open(x, **{'encoding':'utf-8'}) -> rule does NOT fire because encoding present via **kwargs?
# According to spec: rule fires only when no explicit encoding. So this is near-miss.
# Let's do a call that rule WILL fire on, but we inject kwargs that hapen to have encoding via unpacking in a way that rule doesn't see?
# Impossible per spec. Instead, we show what happens if fix is applied incorrectly.
# We'll instead show a case where rule does NOT fire but user might expect it to.

# For hazard: assume rule fires on open(x) and adds encoding, but caller passed **{'encoding':x}
# Not possible statically. So we simulate by having two calls.

print('Skip: rule cannot fire and cause duplicate via **kwargs per spec')

os.remove('test.txt')
