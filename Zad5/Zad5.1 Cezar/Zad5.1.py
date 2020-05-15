def menu():
    ch = int(input("choose one\n1. text to cesar cipher \n2. cesar cipher to text\n"))
    if ch == 1 or ch == 2:
        s = input("enter text\n").upper()
        if if_letters(s):
            n = int(input("enter shift\n"))
            if not n % 26 == 0:
                print(cesar(ch, s, n))
            else:
                print("its the same string!")
        else:
            print("text contain bad characters")
    else:
        print("bad choice")


def if_letters(string):
    for char in range(len(string)):
        if ord(string[char]) < 65 or ord(string[char]) > 90:
            return False
    return True


def cesar(choice, text, shift):
    new_text = ""
    for char in range(len(text)):
        if choice == 1:
            if (ord(text[char]) + shift) > 90:
                new_text += chr(ord(text[char]) + shift - 26)
            else:
                new_text += chr(ord(text[char]) + shift)
        elif choice == 2:
            if (ord(text[char]) - shift) < 65:
                new_text += chr(ord(text[char]) - shift + 26)
            else:
                new_text += chr(ord(text[char]) - shift)
    return new_text


menu()
