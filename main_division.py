import sys
from division_calculator import safe_divide
def main():
    if len(sys.argv) != 3:
        print("usage: python main.py <numerator> <denominator>")
        sys.exit(1)
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    print(safe_divide(numerator, denominator))
if __name__ == "__main__":
    main()