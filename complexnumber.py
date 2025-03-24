class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"

real1 = int(input("Enter real part of first complex number: "))
imag1 = int(input("Enter imaginary part of first complex number: "))
real2 = int(input("Enter real part of second complex number: "))
imag2 = int(input("Enter imaginary part of second complex number: "))

c1 = Complex(real1, imag1)
c2 = Complex(real2, imag2)

sum_result = c1 + c2
mul_result = c1 * c2

print("Sum:", sum_result)
print("Product:", mul_result)
