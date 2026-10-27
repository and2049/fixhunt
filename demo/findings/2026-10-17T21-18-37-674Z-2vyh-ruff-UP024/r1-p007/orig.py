try:
    raise FileNotFoundError("missing")
except OSError:
    print("caught by OSError")
except FileNotFoundError as e:  # THIS IS NOW UNREACHABLE if above except IOError was rewritten to OSError
    print("caught by FileNotFoundError")
