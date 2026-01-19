def main():
    import math

    radius = float(input("Enter the radius of the circle: "))
    circle_area = math.pi * radius ** 2
    print(f"The area of the circle with radius {radius} is {circle_area:.2f}")


if __name__ == '__main__':
    main()