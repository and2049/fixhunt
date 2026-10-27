import typing
# TODO: Add proper type for config when module stabilizes
if typing.TYPE_CHECKING:
    pass
config = {}  # runtime dict, will be typed later
print(f'config={config}')
