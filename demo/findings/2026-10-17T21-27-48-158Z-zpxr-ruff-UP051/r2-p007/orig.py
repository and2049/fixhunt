from __future__ import annotations
import abc

 eval_order = []

def annotate_side_effect():
    eval_order.append('annotated')
    return str

@abc.abstractproperty
def annotated_prop(self) -> 'annotate_side_effect()':  # string ann
    eval_order.append('prop_body')
    return 'value'

# After rewrite: @property\n@abc.abstractmethod
class PropHolder(abc.ABC):
    pass
PropHolder.annotated_prop = annotated_prop

try:
    obj = PropHolder()
    # Access triggers descriptor; annotation not evaluated at call time
    # but if decorator order affected __set_name__ timing...
    val = obj.annotated_prop
    eval_order.append(f'accessed:{val}')
except Exception as e:
    eval_order.append(f'{type(e).__name__}:{e}')

print('|'.join(eval_order))
