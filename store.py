def main():
    products = {
        'apples': 2.99,
        'bananas': 1.50,
        'oranges': 3.25,
        'grapes': 4.00,
        'pears': 2.75
    }

    total_cost = 0

    for item, price in products.items():
        quantity = int(input(f"How many {item} do you want? "))
        total_cost += quantity * price

    print(f"The total cost of your items is: ${total_cost:.2f}")

if __name__ == '__main__':
    main()
