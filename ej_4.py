from interpreter import draw
from chessPictures import *

g1 = square.negative().join(square)

draw(g1.horizontalRepeat(4))