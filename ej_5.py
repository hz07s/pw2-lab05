from interpreter import draw
from chessPictures import *

g1 = square.join(square.negative()).horizontalRepeat(4)
g2 = g1.negative()
g3 = g1.under(g2)

draw(g3.up(g3.negative().horizontalMirror()))