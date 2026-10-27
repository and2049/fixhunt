import re
pattern = r'not\s+.+!='
source = '''not a != b
not(x != y)
'''
matches = re.findall(pattern, source)
print('Matches before fix:', len(matches))
# Simulate after fix: replace not X != Y with X == Y
source_fixed = re.sub(r'not\s+\((.+?)!=(.+?)\)', r'\1 == \2', source)
source_fixed = re.sub(r'not\s+(.+?)!=(.+)', r'\1 == \2', source_fixed)
matches_after = re.findall(pattern, source_fixed)
print('Matches after fix:', len(matches_after))
print('Change in matches:', len(matches) - len(matches_after))
