from interpreter import draw
from chessPictures import *

s = square
sn = square.negative()
g_left = sn.under(rock).join(s.under(knight)).join(sn.under(bishop))
g_right = s.under(bishop).join(sn.under(knight)).join(s.under(rock))
g_mid = s.under(queen).join(sn.under(king))
g_pawn = s.under(pawn).join(sn.under(pawn)).horizontalRepeat(4)
g_square1 = sn.join(s).horizontalRepeat(4)
g_square2 = g_square1.negative()
g_square = g_square1.up(g_square2).verticalRepeat(2)
g_white = g_left.join(g_mid.join(g_right)).up(g_pawn)
g_black = g_pawn.up(g_left.join(g_mid.join(g_right))).negative()

draw(g_white.up(g_square.up(g_black)))