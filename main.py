AddContact = input("Do you want to add a contact? (Y/N): ")

#class definition
class Contact:

    # constructor
    def __init__(self, name, address, phonenumber, birthdate):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.birthdate = birthdate

#adds contact adding
while AddContact == "Y" :

    c = Contact(input("Enter Name: "), input("Enter Address: "), input("Enter Phonenumber: "), input("Enter Birthdate: "))
    t = (c.name, c.address, c.phonenumber, c.birthdate)

    f = open("database.txt", "a")
    f.write('\n' + str(t))
    f.close

    AddContact = input("Do you want to add a contact?: ")


else:
    SearchContact = input("Do you want to search through contacts? (Y/N): ")


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
