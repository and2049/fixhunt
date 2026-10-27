def main():
    path = 'exc.txt'
    try:
        # This open triggers UP015; if 'r' removed, still opens for reading in Py3
        # But we make it so that if the mode were wrong, an error occurs
        # We can't make 'r' removal cause error in Py3, so simulate dependency:
        # Suppose we check that the mode was 'r' via introspection (not possible)
        # Instead: make the open call part of a resource that must be read-only
        f = open(path, 'r')
        raise ValueError('simulated error')
    except ValueError as e:
        print('Caught:', type(e).__name__, str(e))
    finally:
        # If the file was opened for writing by mistake, this would fail
        # But since we only ever open for 'r', and fix doesn't change that,
        # we need a different approach.
        # Let's make the open call happen twice: once in try, once in finally
        try:
            f = open(path, 'r')  # triggers UP015
            f.write('should fail')  # will raise UnsupportedOperation
        except Exception as inner:
            print('Inner error:', type(inner).__name__, str(inner))
        finally:
            if 'f' in locals():
                f.close()
    # Cleanup
    import os
    if os.path.exists(path):
        os.remove(path)
