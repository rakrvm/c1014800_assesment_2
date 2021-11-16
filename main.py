
AddContact = input("Do you want to add a contact? (Y/N): ")


#class definition
class Contact:

    # constructor
    def __init__(self, name, address, phonenumber, birthdate):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.birthdate = birthdate

#ontact adding
while AddContact == "Y" :

    #input for adding contact
    ContactInput = Contact(input("Enter Full Name: "), input("Enter Address: "), input("Enter Phonenumber: "), input("Enter Birthdate: "))
    #stored to use later
    ContactInputStore = ("Name: "+ContactInput.name, "Address: "+ContactInput.address, "Phonenumber:"+ContactInput.phonenumber, "Birthdate: "+ContactInput.birthdate)

    #opens and writes the contact to the file
    f = open("database.txt", "a")
    f.write('\n' + str(ContactInputStore))
    f.close

    AddContact = input("Do you want to add a contact?: (Y/N) ")

else:
    SearchContact = input("Do you want to search through contacts? (Y/N): ")



#searching for contact
while SearchContact == "Y":
    search1 = input("What would you like to search for?: ")
    
##reference : https://stackoverflow.com/questions/18366554/how-to-search-for-word-in-text-file-and-print-part-of-line-with-python
    
    # opening a text file
    f1 = open("database.txt", "r")

    #searching for the line
    for line in f1:
        if search1 in line:
            print(line)


    f1.close()

else:
    EditContact = input("Do you want to edit a contact? (Y/N): ")



while EditContact ==  "Y":
    OriginalVersion = input("What would you like to change?: ")

    f2 = open("database.txt", "r")

    for line in f2:
        if OriginalVersion in line:
            print(line)

    EditedVersion = input("What would you like to change it to?: ")

    with open("database.txt", "r") as file:
        line2 = file.read()
        line2 = line2.replace(OriginalVersion, EditedVersion)
    with open("database.txt", "w") as file:
        file.write(line2)

    EditContact = "N"
