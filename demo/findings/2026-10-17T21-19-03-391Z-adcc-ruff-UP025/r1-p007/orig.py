def f(x: 'u'int') -> None:
    pass
import typing
hints = typing.get_type_hints(f)
print(hints.get('x'))  # Depends on string content; 'u'int'' vs 'int' may be parsed differently by some tools
