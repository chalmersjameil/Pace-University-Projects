def main():
    number = input("enter number")
    number_sum = sum(int(digit) for digit in number )
    print(f'The sum of the number is{number_sum}')
    
    return

if __name__ == '__main__':
    main()