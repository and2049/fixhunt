# This file: mod.py
__all__ = ['public']
private = 42
public = 88
# End mod.py

import os
os.system('python3 -c "\n__all__ = [\"public\"]\nprivate = 42\npublic = 88\n" > mod.py')

from mod import *  # imports only public
print('after star-import: public=', public, 'private exists?', 'private' in dir())

# Now simulate: setattr(mod, '__all__', ['private']) triggers rule
import mod
mod.__all__ = ['private']  # rule fires
print('after setattr __all__:', mod.__all__)

# Now star-import again: should import private
from mod import *
print('after second star-import: public=', public, 'private=', private if 'private' in locals() else 'not imported')
os.remove('mod.py')
