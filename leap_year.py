def main():
    year_input = input("Enter a year: ")
    
    def leap_year(year):
        if year.isdigit():
            year = int(year)
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print("Invalid input. Please enter a valid year.")
    
    leap_year(year_input)

if __name__ == '__main__':
    main()