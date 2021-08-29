import usys
import unittest

usys.path.insert(1, 'src')
from ferris_wheel.config import FerrisWheelConfig

class TestFerrisWheel():
    pass

print(usys.path)