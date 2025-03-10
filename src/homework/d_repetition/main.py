from repetition import get_factorial
from repetition import sum_odd_numbers


def main():
    while True:
        print("\n=== Homework 3 Menu ===")
        print("1 - Factorial")
        print("2 - Sum of odd numbers")
        print("3 - Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            handle_factorial()
        elif choice == "2":
            handle_sum_odd_numbers()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

    
def handle_factorial():
    while True:
        try:
            num = float(input("Enter a number for factorial (1-9): "))
            if num.is_integer():
                num = int(num)
            else:
                print("The entered number is not an integer. Please try again.")
                continue

            if 1 <= num < 10:
                print(f"Factorial of {num} = {get_factorial(num)}")
                break
            else:
                print("Number must be between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if not ask_continue():
        exit()

def handle_sum_odd_numbers():
    while True:
        try:
            num = float(input("Enter a number for the sum of odd numbers (1-99): "))
            num = int(num)

            if 1 <= num < 100:
                print(f"Sum of odd numbers up to {num} = {sum_odd_numbers(num)}")
                break
            else:
                print("Number must be between 1 and 99.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if not ask_continue():
        exit()

def ask_continue():
    while True:
        choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            print("Exiting program...")
            return False
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
