class Calculator:
    count = 0  # static attribute to track usage

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Demonstration
print("Sum:", Calculator.add(5, 3))
print("Sum:", Calculator.add(10, 15))
print("Add method called:", Calculator.count, "times")
