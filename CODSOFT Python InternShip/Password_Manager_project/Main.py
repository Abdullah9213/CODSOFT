from Password_Manager import generate_defined_password, generate_predefined_password, generate_random_password


def main():
    print("===Password Generator===")
    print("------------------------")
    length = int(input("Enter the desired length of the password: "))
    while True:
        print("===Password Complexity Choice===")
        print("1. Define Complexity of password")
        print("2. Use Predefined Complexity of password")
        print("3. Generate Random password")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            while True:
                upper_count = int(input("Enter the number of upper case letters: "))
                lower_count = int(input("Enter the number of lower case letters: "))
                digit_count = int(input("Enter the number of digits: "))
                special_count = int(input("Enter the number of special characters: "))

                if upper_count + lower_count + digit_count + special_count != length:
                    print("Error: Total count of characters must match the length of the password.")
                else:
                    break
            password = generate_defined_password(length, upper_count, lower_count, digit_count, special_count)
            break
        elif choice == 2:
            password = generate_predefined_password(length)
            break
        elif choice == 3:
            password = generate_random_password(length)
            break
        elif choice == 4:
            print("Thank you for using Password Generator")
            return

    print("Generated Password:", password)


if __name__ == "__main__":
    main()
