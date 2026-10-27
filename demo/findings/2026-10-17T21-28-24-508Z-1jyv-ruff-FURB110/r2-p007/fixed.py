class Sensor:
    def __init__(self):
        self._reads = 0
    @property
    def reading(self):
        self._reads += 1
        return self._reads  # 1,2,3,...
s = Sensor()
# First, access s.reading to get a truthy value (1)
_first = s.reading  # now _reads=1
# Condition: s.reading -> property access
alarm = s.reading or 0
print('sensor_reads:', s._reads, 'alarm:', alarm)
# Original: two property gets -> _reads increases by 2 (from 1 to 3), alarm = second reading (3)
# Fixed: one property get -> _reads increases by 1 (to 2), alarm = that value (2)
# Output: original alarm=3, fixed alarm=2 -> different
