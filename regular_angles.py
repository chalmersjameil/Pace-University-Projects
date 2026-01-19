def main():
    num_sides = int(input("Enter the number of sides of the polygon: "))
    exterior_angle = 360 / num_sides
    interior_angle = 180 - exterior_angle
    print(f"The exterior angle of the polygon is {exterior_angle:.2f} degrees.")
    print(f"The interior angle of the polygon is {interior_angle:.2f} degrees.")    
    
    return

if __name__ == '__main__':
    main()