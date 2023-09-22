import sys
print(sys.path)
sys.path = ['.']
print(sys.path)
from .sem4_5 import adder
