#  minh tran

def encode(unencoded_string: str):
    unencoded_string = str(unencoded_string)
    encoded_string: str = ""
    for index in range(len(unencoded_string)):
        encoded_string += str(int(unencoded_string[index]) + 3)
    return encoded_string


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


def main():
    option = ""
    while option != "3":
        option = input("1: encode a password \n2: decode a password \n3: exit\nenter an option: ")

        if option == "1":
            print(f"your encoded password is: {encode(input("enter a password to decode "))}")
        if option == "2":
            print(f"your decoded password is: {decode(input("enter a password to decode "))}")

    print("bye")


if __name__ == "__main__":
    main()
