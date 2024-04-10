
#riley
def encode(password):
    #riley johnson
    encoded = ""
    for i in password:
        i = int(i)
        if i == 7:
            i = "0"
        elif i == 8:
            i = "1"
        elif i == 9:
            i = "2"
        else:
            i += 3
            i = str(i)
        encoded += i
    return encoded

if __name__ == "__main__":
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 3:
            break
        elif option == 1:
            pass_to_encode = input("Please enter your password to encode: ")
            encode(pass_to_encode)
            print("Your password has been encoded and stored!\n")