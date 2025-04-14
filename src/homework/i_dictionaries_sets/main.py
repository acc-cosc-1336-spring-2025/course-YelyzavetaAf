import dictionary

def main():
    widgets = {}

    while True:
        print("\nInventory Menu")
        print("1 - Add or update Item")
        print("2 - Delete Item")
        print("3 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter widget name: ")
            quantity = int(input("Enter quantity: "))
            dictionary.add_inventory(widgets, name, quantity)
            print(f"Updated inventory: {widgets}")
        elif choice == "2":
            name = input("Enter widget name to delete: ")
            result = dictionary.remove_inventory_widget(widgets, name)
            print(result)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")
if __name__ =="__main__":
    main()