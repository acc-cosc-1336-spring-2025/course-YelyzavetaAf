from class_a import Die

def main():
    die = Die()
    keep_rolling = True
    while keep_rolling:
        die.roll()
        print(die)
        answer = input("Roll again? (y/n): ").lower()
        if answer != 'y':
            keep_rolling = False

if __name__ == "__main__":
    main()