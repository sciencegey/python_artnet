'''Simple library that takes Artnet (DMX) packets and converts them to data that Python can use.'''
__version__ = "1.0.0"
debug = False   # Global debug flag
from .python_artnet import Artnet