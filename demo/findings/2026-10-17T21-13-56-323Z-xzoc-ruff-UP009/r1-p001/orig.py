# -*- coding: utf-8 -*-
class A:
    x = 1
    @property
    def y(self):
        return self.__class__.x + 1
try:
    print(A().y)
except Exception as e:
    print(type(e).__name__, str(e))
