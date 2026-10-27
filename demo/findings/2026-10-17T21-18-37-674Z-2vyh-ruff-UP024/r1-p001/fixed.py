# This comment explains why we handle IOError
# Specifically for legacy file operations
raise OSError("legacy error")  # Keep this message
