# Relative path specification -- Good enough for publishing concise packages
from .arithmetic import *
from .logarithm import *


# Absolute paths - Generally used in places where the current file could be moved in future, 
# thereby disturbing the relative path/reference
import sys
print(f"{sys.path=}")
# sys.path.append("SomePath")
