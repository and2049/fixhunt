__all__ = ['flag']
flag = False if 1 == 1 else True
print('flag before import:', flag)
# Simulate star import effect
locals().update({'flag': not flag})
print('flag after simulated * import:', flag)
