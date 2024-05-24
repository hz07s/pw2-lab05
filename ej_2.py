from interpreter import draw
from chessPictures import *

g1 = knight.join(knight.negative())
g2 = g1.verticalMirror()

draw(g1.up(g2))