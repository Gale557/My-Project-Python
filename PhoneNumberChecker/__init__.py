def phonenumber(contact):
    length = len(contact)
    first = contact[0]
    second = contact[1]
    if length == 12:
        if contact.isnumeric():
            if first == "0" and second == "8":
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")

