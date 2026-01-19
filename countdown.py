import time

def countdown():
    while True:
        try:
            seconds = int(input("Enter the number of seconds to count down: "))
            if seconds < 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    while seconds:
        print(f"{seconds} seconds remaining.")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    countdown()

if __name__ == '__main__':
    main()
