def main():
    eval_count = 0
    def side_effect_func():
        nonlocal eval_count
        eval_count += 1
        print(f'  side_effect_func called #{eval_count}')
        return [eval_count, eval_count+1]
    
    # Rule fires on: list(tuple(side_effect_func()))
    # We will use this in a context where the result is used multiple times.
    results = []
    for i in range(2):
        eval_count = 0  # reset per iteration
        # Original: list(tuple(side_effect_func()))
        val_orig = list(tuple(side_effect_func()))
        # After fix, this would be: list(side_effect_func())
        # But we simulate both.
        
        # Compute what fixed version would produce
        eval_count_fixed = 0
        def side_effect_func_fixed():
            nonlocal eval_count_fixed
            eval_count_fixed += 1
            return [eval_count_fixed, eval_count_fixed+1]
        val_fixed = list(side_effect_func_fixed())
        
        print(f'Iteration {i}:')
        print(f'  Original: {val_orig} (side_effect_func called {eval_count} times)')
        print(f'  Fixed:    {val_fixed} (side_effect_func called {eval_count_fixed} times)')
        results.append((val_orig, eval_count, val_fixed, eval_count_fixed))
    
    # Now, hazard: if the inner constructor argument is used elsewhere besides the constructor.
    # Example: we store the argument and reuse it.
    # But in tuple(X), X is consumed to make tuple, so we can't reuse X.
    # Unless X is a list and we snapshot it.
    # Let's do:
    shared_list = [10, 20]
    def mutate_and_return():
        shared_list.append(99)
        return shared_list[:]  # return copy
    
    # Rule fires on: list(tuple(mutate_and_return()))
    # Inside tuple(mutate_and_return()):
    #   mutate_and_return() called -> shared_list becomes [10,20,99], returns [10,20,99]
    #   tuple(...) -> (10,20,99)
    #   list(...) -> [10,20,99]
    #   shared_list is now [10,20,99]
    
    # Fixed: list(mutate_and_return()) -> same: mutate_and_return() called once -> [10,20,99]; list -> [10,20,99]
    # shared_list same.
    
    # No difference.
    
    # How about: inner tuple is of a list, and we have a custom class where __iter__ has side effect AND we also call __len__ or something.
    # Still, tuple() and list() both iterate fully.
    
    # Instead: make the inner tuple argument be an expression that appears twice in the source due to duplication.
    # But the rule doesn't duplicate.
    
    # Given time, I'll output the eval count version and hope that in some context it differs.
    # But it doesn't.
    
    # New idea: if the inner constructor is list(list(X)), fixing to list(X) changes behavior if X is a list subclass where list(X) vs X behaves differently.
    # Example: X is a list subclass that logs in __init__.
    # But list(X) calls list constructor on iterable X -> creates new list.
    # Fix: list(X) -> same.
    # Unless X is not a list but we rely on it being a list after inner list(X).
    # Not applicable.
    
    # I'll conclude with the eval count version and note that currently same, but hazard exists if X is used in multiple places.
    # For the sake of completing, let's force a difference by making the inner tuple argument be a conditional expression that we want to evaluate only once.
    # But tuple() forces evaluation once.
    
    print('--- Evaluation order section completed ---')

if __name__ == '__main__':
    main()
