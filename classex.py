class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def getNumber(self):
        if self.imag >= 0:
            print(f'{self.real}+j{self.imag}')
        else:
            print(f'{self.real}-j{-self.imag}')

num1 = ComplexNumber(2, 3)
num1.getNumber()
