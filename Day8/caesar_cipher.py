import random

def cipher():
    def caesar(choice,msg,shift_num):
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'X', 'W', 'Y', 'Z']
        en_msg = ""
        for i in msg:
            if choice == "decode":
                en_msg += alpha[(alpha.index(i)-shift_num) % len(alpha)]
            else:
                en_msg += alpha[(alpha.index(i)+shift_num) % len(alpha)]
        return en_msg

    choice = input("What do you want to do? Type 'encode' - encrypt and 'decode' - decrypt:  ")
    msg = input("Enter the message: ")
    shift_num = random.choice(range(1,52))
    print(f"{choice}ed result is {caesar(choice,msg,shift_num)}")
    
    print("Do you want to try again? Type 'Yes' or 'No': ",end=" ")
    again = input().lower()

    if again == "yes":
        cipher()
    elif again == "no":
        print("Thank you! Try later")
    else:
        print("Invalid Input")

cipher()
