#This is test file No 2
from test1 import Base

class Derived(Base):
    def baz(self):
        return 'baz'

print("test")