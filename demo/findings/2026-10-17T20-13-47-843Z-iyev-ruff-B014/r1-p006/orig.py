try:
    [] + {}
except (TypeError, Exception):  # TypeError is more specific
    print('type error')
