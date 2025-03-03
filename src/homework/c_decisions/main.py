from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

def main():
    option = int(input("Enter the number of options: "))
    total = int(input("Enter the total number: "))

    try:
        ratio = get_options_ratio(option, total)
        rating = get_faculty_rating(ratio)

        print(f"Ratio: {ratio:.2f}")
        print(f"Faculty Rating: {rating}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()