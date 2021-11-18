


#Adding a new contact to the text file
def AddToFile (Data):
    print(Data)

# Retrieving all the Contacts and adding them into a 2D array
def RetrieveData():
    pass

# Function to View all contacts
def ViewAllContacts():
    pass


def PostCodeChecker():
    PostCode = input("What is your Post Code ?")
    PostCodeNoSpace = PostCode.replace(" ","")

    if len(PostCodeNoSpace)>6 or len(PostCodeNoSpace)<5:
        print("this is an invalid Post Code ")
        PostCodeChecker()
    else:
        return PostCode

#Creating a New Contact with verifying for each data point 
def CreateContact():
    NewContact = ["","","","","",""]
    Verify = False
    while Verify == False:
        First = input("What is your First Name ?")
        if len(First) < 1:
            print("Invalid Input")
        else:
            NewContact[0] = First
            Verify = True

    Verify = False
    while Verify == False:
        Last = input("What is your Last Name ?")
        if len(Last) < 1:
            print("Invalid Input")
        else:
            NewContact[1] = Last
            Verify = True

    NewContact[2] = PostCodeChecker()
    NewContact[3] = NumberFunction(0,10000,"What is your House Number ?")
    NewContact[4] = NumberFunction(911,999999999999999, "What is your Phone Number ?")
    NewContact[5] = input("What is you Birth Date (use format DD-MM-YYYY) ?")

    AddToFile(NewContact)

# Function to delete a contact
def DeleteContact():
    pass

#Function to edit contacts
def EditContacts():
    pass

#Function for Searching for Contact
def SearchContact():
    pass

#Verifies a user input is a number with parameters
def NumberFunction( Min, Max, Message):
    Verify = False
    while Verify == False:
        Input = input(Message)
        #is try statement checks the users input is a valid integer
        try:
            Input = int(Input)
            Verify = True
        except:
            print("This is not a Valid Integer")
        # If the input has been approved as an integer it checks it between the min and max values
        if Verify == True:
            if Min <= Input and Input <= Max:
                Verify = True
            else:
                print("This is not a Valid Option")
                Verify = False
    return Input


def Main():
    RetrieveData()
    print("CONTACTS")
    print("---------------------")
    print("1. View All Contacts ")
    print("2. Create Contacts")
    print("3. Delete Contacts")
    print("4. Edit Contacts")
    print("5. Search Contacts")
    print("6. Close application ")

    Userinput = NumberFunction(1,6,"Please select an option - ")
    print("You have selected option" , Userinput)
    if Userinput == 1:
        ViewAllContacts()
    if Userinput == 2:
        CreateContact()
    if Userinput == 3:
        DeleteContact()
    if Userinput == 4:
        EditContacts()
    if Userinput == 5:
        SearchContact()
    if Userinput == 6:
        quit()

Main()
