from typing import Literal

"""Module docstring."""

x = Literal[
    Literal['alpha'],  # Keep this
    Literal['beta']    # Remove this line? No, we keep both.
]
"""This is a docstring for x"""
print(x.__args__)
