def main():
    import random 
    roll = [random.randint(1,6) for i in range(10)]

    average = sum(roll) / len(roll)

    print(f"The average of dice rolls is{average}")

    
    return

if __name__ == '__main__':
    main()