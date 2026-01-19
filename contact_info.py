def main():
    contacts = {'Alice': '555-1234', 'Bob': '555-5678', 'Charlie': '555-8765'}

    name = input("Enter a name: ")
    if name in contacts:
        print(f"{name}'s phone number: {contacts[name]}")
    else:
        print(f"Contact not found for {name}")

if __name__ == '__main__':
    main()
