from decisions import get_options_ratio, get_faculty_rating

def main():
    try:

        option = int(input("Enter the number of options: "))
        total = float(input("Enter the total number: "))
        if total == 0:
            print("Error: Total number cannot be zero.")
            return

    
        ratio = get_options_ratio(option, total)
        rating = get_faculty_rating(ratio)

        print(f"Ratio: {ratio:.2f}")
        print(f"Faculty Rating: {rating}")

    except ValueError as e:
        print(f"Error: Invalid input! {e}")

if __name__ == "__main__":
    main()