def main():
    import random 
        
    sides = int(input("Number of sides the dice has: "))
    side = random.randrange(1,sides)
    print(f"You rolled a {side}")        

    

if __name__ == '__main__':
    main()