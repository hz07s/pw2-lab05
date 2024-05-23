from colors import *
class Picture:
    def __init__(self, img):
        self.img = img;

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        new_img = self.img[::-1]
        return Picture(new_img)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        new_img = []
        for line in self.img:
            new_img.append("".join(self._invColor(char) for char in line))
        return Picture(new_img)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        new_img = [self_line + p_line for self_line, p_line in zip(self.img, p.img)]
        return Picture(new_img)

    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura recibida como argumento,
            encima de la figura actual """
        new_img = p.img + self.img
        return Picture(new_img)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        new_img = [''.join([self_char if p_char == ' ' else p_char for self_char, p_char in zip(self_line, p_line)]) for self_line, p_line in zip(self.img, p.img)]
        return Picture(new_img)
  
    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        if n < 1:
            return Picture(self.img)
        new_img = [line * n for line in self.img]
        return Picture(new_img)

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual debajo, 
            la cantidad de veces que indique el valor de n """
        if n < 1:
            return Picture(self.img)
        new_img = [line for _ in range(n) for line in self.img]
        return Picture(new_img)

    #Extra: Sólo para realmente viciosos 
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        return Picture(None)

