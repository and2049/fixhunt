debug_mode = False  # Set via deploy script
if debug_mode:
    pass  # Enable verbose logging in dev
print('Debug comment preserved:', 'verbose logging' in open(__file__).read())
