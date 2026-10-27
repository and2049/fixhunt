# This tests detection robustness: ensure u-only triggers on strings
val = 42
u_val = u'42'  # should trigger
print('val == int(u_val)?', val == int(u_val))
print('u_val type:', type(u_val))
# If rule misfires on 'u_val = u42', SyntaxError would occur - we avoid that.
