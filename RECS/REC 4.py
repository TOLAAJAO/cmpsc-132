# Recitation Activity 4
# Omotola AJAO
# Section 002R
# oaa5544@psu.edu

class Complex:

    def __init__(self, r, i):
        self._real = r
        self._imag = i

    def __str__(self):
        if self._imag >= 0:
            return f"{self._real} + {self._imag}i"
        else:
            return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__

    def conjugate(self):
        return Complex(self._real, -1 * self._imag)

    def __mul__(self, other):

        if isinstance(other, Complex):
            real_part = self._real * other._real - self._imag * other._imag
            imag_part = self._imag * other._real + self._real * other._imag
            return Complex(real_part, imag_part)

        else: 
            return Complex(self._real * other, self._imag * other)

    def __rmul__(self, other):
        return self * other
    
class Real(Complex):

    def __init__(self, r):
        super().__init__(r, 0)

    def __mul__(self, other):

        if isinstance(other, Real):
            result = super().__mul__(other)
            return Real(result._real)

        elif isinstance(other, (int, float)):
            result = super().__mul__(other)
            return Real(result._real)

        elif isinstance(other, Complex):
            return super().__mul__(other)

        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Real):
            return self._real == other._real

        elif isinstance(other, Complex):
            return self._real == other._real and other._imag == 0

        else:
            return False

    def __int__(self):
        return int(self._real)

    def __float__(self):
        return float(self._real)

