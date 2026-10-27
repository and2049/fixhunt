def main():
    tuple = list  # Shadow tuple in local scope
    def inner():
        tuple = lambda x: [x*2]  # Further shadow
        return tuple([1, 2])  # Returns [2, 4]
    # Rule fires on: list(tuple([1, 2]))  -> but wait, inner tuple is lambda
    # We need: list(tuple(X)) where tuple refers to the shadowed one.
    # So: define tuple as something, then use it.
    # Let's reset.
    del tuple  # remove shadow
    
    tuple = list  # global shadow
    def test():
        # Rule fires on: list(tuple([1, 2]))
        # Here, tuple is list (from outer scope)
        # So tuple([1,2]) -> list([1,2]) -> [1,2]
        # Then list([1,2]) -> [1,2]
        # Fix: list([1,2]) -> [1,2]
        # Same.
        # But if we had: tuple(tuple([1,2])) and outer tuple is something else...
        # Not our pattern.
        # Instead, make the shadowed tuple act differently.
        tuple = lambda x: x + [99]  # local tuple that appends 99
        try:
            res = list(tuple([1, 2]))  # tuple([1,2]) -> [1,2,99]; list -> [1,2,99]
            print('list(tuple([1,2])):', res)
        except Exception as e:
            print('Error:', type(e).__name__, str(e))
        
        # What fix would produce: list([1,2]) -> [1,2]
        try:
            res2 = list([1, 2])
            print('list([1,2]):', res2)
        except Exception as e:
            print('Error:', type(e).__name__, str(e))
        
        # Now, to see if the inner tuple call is affected by shadowing:
        # We already used local tuple.
        # Also test: if we remove the outer list, does it change which tuple is used?
        # No, inner tuple(...) is still using the locally shadowed tuple.
        
        # But the hazard is: removing outer call may change which tuple is invoked.
        # How? Only if the inner tuple(...) was meant to call the global tuple, but shadowing makes it call local.
        # And removing outer list doesn't change that.
        
        # Unless: we have nested scopes where the inner tuple resolves differently based on context.
        # Example:
        tuple = list  # level 1 shadow
        def middle():
            tuple = tuple  # level 2: refers to level 1 tuple (which is list)
            def inner():
                # Rule fires on: list(tuple([1,2]))
                # Here, tuple refers to level 2 tuple -> level 1 tuple -> list
                return list(tuple([1, 2]))
            return inner()
        
        print('middle():', middle())
        
        # Fix would make inner() return list([1,2]) -> same.
        
        # To get a change, we need the inner tuple to refer to one thing, and after fix,
        # the expression list(X) refers to tuple in a different scope?
        # Impossible.
        
        # Final attempt: make the inner tuple(...) be a tuple constructor call,
        # but we have shadowed tuple, so it fails, and we catch it.
        # Then, if fix removes outer list, we might have X alone, which could be used.
        # But our pattern is list(tuple(X)) -> fix to list(X).
        # If tuple(X) raises, then list(tuple(X)) never completes; fix would try list(X).
        # So if X is list-like, list(X) might work.
        
        # Example:
        tuple = 999  # shadow with int
        try:
            list(tuple([1, 2]))  # tuple([1,2]) -> 999([1,2]) -> TypeError
        except TypeError as e:
            print('tuple is int error:', type(e).__name__, str(e))
        
        # Fix would produce: list([1,2]) -> [1,2] -> works
        try:
            list([1, 2])
            print('list([1,2]) works:', [1,2])
        except Exception as e:
            print('Error:', type(e).__name__, str(e))
        
        # Now we have a behavioral difference!
        # Before fix: TypeError
        # After fix: [1,2]
        # And the rule fires on list(tuple([1,2])) because syntactically it looks like tuple(callable).
        # Even though at runtime tuple is 999, the linter doesn't know.
        
        # Let's build full program around this.

if __name__ == '__main__':
    main()
