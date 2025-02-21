from polymorphism_demo import shape, rectangle, circle
import math

def main():
    shapes = [
        rectangle(10, 5),
        circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()