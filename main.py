#  minh tran

def encode(unencoded_string: str):
    unencoded_string = str(unencoded_string)
    encoded_string: str = ""
    for index in range(len(unencoded_string)):
        encoded_string += str(int(unencoded_string[index]) + 3)
    return encoded_string


"""def decode(encoded_string: str):
    encoded_string = str(encoded_string)
    unencoded_string = ""
    for index in range(len(encoded_string)):
        unencoded_string += str(int(encoded_string[index]) - 3)
    return unencoded_string"""


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
