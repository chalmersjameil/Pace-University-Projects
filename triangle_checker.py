def is_triangle(a, b, c):
    sides = sorted([a, b, c])
    
    if sides[0] + sides[1] > sides[2]:
        print("Valid Triangle")
        if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
            print("Right Triangle")
        else:
            print("Not a Right Triangle")
    else:
        print("Not a Triangle")

def main():
    a, b, c = [float(input(f"Enter side {i}: ")) for i in range(1, 4)]
    is_triangle(a, b, c)

if __name__ == '__main__':
    main()
