class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value - other.value)
        return NotImplemented

    def __str__(self):
        return str(self.value)

num1 = CustomNumber(10)
num2 = CustomNumber(5)

sum_result = num1 + num2
sub_result = num1 - num2

print("Sum:", sum_result)
print("Subtraction:", sub_result)
