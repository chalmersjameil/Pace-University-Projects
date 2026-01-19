def main():
    num_strings = ['12', '4789', '1010', '111111', '43216', '2934', '9999', '987654321', '123123123123', '1291212', '98987989']
    number_aggregator(num_strings)
    
def number_aggregator(numbers):
    aggregate = []
    
    for num in numbers:
        even_sum = sum(int(digit) for digit in num if int(digit) % 2 == 0)
        odd_product = 1
        has_odd = False
        
        for digit in num:
            if int(digit) % 2 != 0:
                odd_product *= int(digit)
                has_odd = True
        
        odd_product = odd_product if has_odd else 0
        aggregate.append(abs(even_sum - odd_product))
    
    print("Results:", aggregate)

if __name__ == "__main__":
    main()
