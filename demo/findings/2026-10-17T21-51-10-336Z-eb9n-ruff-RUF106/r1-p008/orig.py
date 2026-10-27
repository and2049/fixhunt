##
# This section covers error handling (see RFC 999)
# ruff: ignore[E501]  # Line too long in doc example
# See also: @ref error-handling
value = 'error'
print('loaded' if value else 'failed')
