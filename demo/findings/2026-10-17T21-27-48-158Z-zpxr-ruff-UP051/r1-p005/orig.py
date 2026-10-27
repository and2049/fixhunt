import abc
# This comment should stay
@abc.abstractclassmethod
    """This docstring should be preserved."""
    def meth(cls):
        return 'preserved'
print('Docstring:', meth.__func__.__doc__)
# Check if comment proximity affects anything—no runtime effect, but we trace via doc
