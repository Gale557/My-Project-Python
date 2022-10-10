import PhoneNumberChecker
n = int(input("Input How Many PhoneNumber: "))


for i in range(1, n + 1):
    contact = str(input(f"{i} : "))
    PhoneNumberChecker.phonenumber(contact)
