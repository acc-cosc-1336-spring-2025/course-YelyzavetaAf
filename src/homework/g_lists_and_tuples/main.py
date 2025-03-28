from lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("\n1 - Show the list low/high values")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "2":
            print("Exiting program...")
            break
        elif choice == "1":
            numbers = []
            while True:
                try:
                    value = int(input("Enter a list value: "))
                    numbers.append(value)
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if len(numbers) >= 3:
                    more = input("Do you want to enter another value? (y/n): ")
                    if more.lower() != 'y':
                        break

            print("Lowest value:", get_lowest_list_value(numbers))
            print("Highest value:", get_highest_list_value(numbers))
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

        