import pathlib
p = pathlib.Path('nonexistent.txt')
print('Path exists:', p.exists())
print('Exists == True:', p.exists() == True)
print('not exists:', not p.exists())
# Create then delete to show change
p.touch()
print('After touch - exists == True:', p.exists() == True)
print('After touch - not exists:', not p.exists())
p.unlink()
