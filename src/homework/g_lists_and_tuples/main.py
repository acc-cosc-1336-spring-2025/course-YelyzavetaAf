from lists import get_lowest_list_value, get_highest_list_value, get_p_distance_matrix

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
       


def get_matrix_menu():
    dataset = [
        ['T','T','T','C','C','A','T','T','T','A'],
        ['G','A','T','T','C','A','T','T','T','C'],
        ['T','T','T','C','C','A','T','T','T','T'],
        ['G','T','T','C','C','A','T','T','T','A']
    ]

    while True:
        print("\nMenu:")
        print("1 - Get p distance matrix")
        print("2 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            matrix = get_p_distance_matrix(dataset)
            print("\nP-Distance Matrix:")
            for row in matrix:
                print(" ".join(f"{val:3f}" for val in row))
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
if __name__ == "__main__":
    get_matrix_menu()