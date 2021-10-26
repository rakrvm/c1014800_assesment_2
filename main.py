# class definition
class Contact:

    # constructor
    def __init__(self, name, address, phonenumber, birthdate):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.birthdate = birthdate

if __name__== "__main__":

    c = str(Contact(input(str("Enter Name: ")), input(str("Enter Address: ")), input(str("Enter Phonenumber: ")), input(str("Enter Birthdate:"))))
    t = (c.name.append, c.address, c.phonenumber, c.birthdate)

    f = open("database.txt")
    f.write(t)
    f.close()
