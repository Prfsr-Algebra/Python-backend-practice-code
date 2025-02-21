def safe_divide(numerator, denominator):
    try:
        try:
            if denominator != 0:
                 return float(numerator) / float(denominator)
        except ValueError as e:
            return "Enter numeric values only"
    except ZeroDivisionError as e:
        return "error! cannot divide by zero"
    