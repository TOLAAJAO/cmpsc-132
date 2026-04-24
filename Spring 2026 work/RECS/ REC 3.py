# Recitation Activity 3
# Omotola AJAO
# Section 002R
# oaa5544@psu.edu


class Complex:
    """
        >>> a = Complex(5,-6)
        >>> b = Complex(2,14)
        >>> a*b
        94 + 58i
        >>> b*5
        10 + 70i
        >>> 5*b
        10 + 70i
        >>> isinstance(5*b, Complex)
        True
        >>> a.conjugate()
        5 + 6i
        >>> b.conjugate()
        2 - 14i
    """

    def __init__(self, r, i):
        self._real = r
        self._imag = i

    def __str__(self):
        if self._imag >= 0:
            return f"{self._real} + {self._imag}i"
        return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__

    def conjugate(self):
        return Complex(self._real, -self._imag)

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self._real * other._real - self._imag * other._imag
            imag_part = self._real * other._imag + self._imag * other._real
            return Complex(real_part, imag_part)
        elif isinstance(other, (int, float)):
            real_part = self._real * other
            imag_part = self._imag * other
            return Complex(real_part, imag_part)
        return NotImplemented

    def __rmul__(self, other):
        return self * other


def run_tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    run_tests()
