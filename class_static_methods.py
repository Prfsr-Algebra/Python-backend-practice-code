class calculator:
    calculation_type = "multiplication"
    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def multiply(cls, a, b):
        print(f"calculation type: {cls.calculation_type}")
        return a * b
