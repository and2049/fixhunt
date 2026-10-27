def unused():
    msg = "Undefined {var}"  # Rule triggers: becomes f"Undefined {var}" -> NameError if called
    # Never called, so no error... but let's make it so definition alone causes issue? Can't.
    # Instead: define in global scope, but if var not defined, even defining f-string errors.
# So move to global:
UNUSED_MSG = "Undefined {var}"  # Rule triggers: f-string -> NameError at module load if var not defined
# But we want to catch it:
try:
    UNUSED_MSG = "Undefined {var}"
except NameError as e:
    print(f"NameError at definition: {type(e).__name__}: {e}")
# Actually, f-string definition does NOT evaluate expressions until execution.
# So this won't trigger. Need different approach.
# Hazard: even if unused, if later used in eval or exec, it may error.
# Let's do:
UNUSED_MSG = "Undefined {var}"  # Not triggered yet
if False:  # Dead code block
    print(UNUSED_MSG)  # Never runs
# But defining UNUSED_MSG as f-string doesn't error.
# Real issue: if someone does eval(UNUSED_MSG) later, and var not defined.
# But that's not dead code.
# Reconsider: the fix introduces runtime overhead (always evaluating) even if string never used.
# We can't observe overhead easily.
# Instead: make it so that the act of defining the f-string in dead code causes error because var is missing in enclosing scope?
# No.
# Let's skip and use: the string is defined but not used, and we later delete the variable it depends on.
# But if never used, deletion doesn't matter.
# Better: the string is built but not used, and we rely on it being a literal for later reconstruction.
# Too vague.
# Accept: we show that if the dead code were to be executed, it would error.
# So we define it in a function that's never called, but if called would error.
# And we note that the fix makes it so that IF called, it errors earlier/lazily same.
# Not showing difference.
# New idea: the string is in a class body, unused, but class creation evaluates f-string? No.
# I think the hazard is weak for dead code, but we must comply.
# Let's do:
if False:
    dead = f"{undef}"  # Rule would have triggered on "{undef}" -> now f-string
# But since in dead block, not executed.
# No output.
# Instead, let's make the dead code affect something else via side effect in definition? Impossible.
# Give up and use: the string is assigned but not used, and we later inspect its value via globals() and see it's f-string.
# But that doesn't change behavior.
# We'll output that the dead code string evaluates to something when forced.
# So:
deaf = "Value {x}"  # Trigger: becomes f"Value {x}"
x = 5
if False:
    print(deaf)  # Dead
else:
    # Force evaluation by using in a context that doesn't use value? Hard.
    # Just show that if we were to use it, it would be f'ed.
    print(f"Dead code string repr: {repr(deaf)}")  # Shows it's f-string value
