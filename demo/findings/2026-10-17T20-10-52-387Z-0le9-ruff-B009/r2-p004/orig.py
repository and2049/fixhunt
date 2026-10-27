from typing import TYPE_CHECKING
if TYPE_CHECKING:
    x = getattr(__import__('os'), 'path')  # rule fires here
else:
    class A: pass
    a = A()
    # Simulate runtime use of annotated name
    def f():
        return getattr(a, '__class__')
    print(f())
# Note: The fix would rewrite the TYPE_CHECKING block, but it's skipped at runtime
# So no behavioral change? Need to make it affect runtime.
# Let's instead use a string annotation that gets evaluated.
