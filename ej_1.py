from interpreter import draw
from chessPictures import *

g1 = knight.join(knight.negative())
g2 = knight.negative().join(knight)

draw(g1.up(g2))