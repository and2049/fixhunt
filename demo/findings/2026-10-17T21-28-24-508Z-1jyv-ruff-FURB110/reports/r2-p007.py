class Sensor:
    def __init__(self):
        self._reads = 0
    @property
    def reading(self):
        self._reads += 1
        return self._reads  # 1,2,3,...
s = Sensor()
alarm = s.reading if s.reading else 0
print('sensor_reads:', s._reads, 'alarm:', alarm)
