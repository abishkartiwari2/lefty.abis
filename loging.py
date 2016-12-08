print("Patient Management System")
print("Login Process")

phy_file="demo.txt"


def confirm( patientId, firstName, lastName, address, gender, contact):
    now= open(phy_file,'a')
    now.write("%16s%16s%16s%16s%16s%16s\n" % (patientId, firstName, lastName, address, gender, contact))
    now.close()

def must():
    login= input("1. Login Physician\n2. Login Accountant")
    if login == "1":
        userName = input("Username\n")
        passWord = input("Password\n")
        print("Successfully Login")
        while True:
            another = input("Main Menu - Select Patient\n1. New Patient\n2. Old Patient ")
            if another=="1":
                print("Create an account")
                patientId = input("PaientID")
                firstName = input("Firstname")
                lastName = input("Lastname")
                address = input("Address")
                gender = input("Gender")
                contact = input("Contact")
                confirm(patientId, firstName, lastName, address, gender, contact)
                print("Successfully Register")
                noise= input("Press enter to go on main menu")
            if another=="2":
                now = open(phy_file,'r')
                number = input("PatientID")
                for line in now:
                    (patientId, firstName, lastName, address, gender, contact) = line.split()
                    if (patientId == number):
                        print(patientId, firstName, lastName, address, gender, contact)
                now.close()
                print("Do you want to take appointment(1 or 2)?\n")
                choose = input("1. Yes\n2. No")
                if choose == "1":
                    print("Take appointment\nList of the doctors\n")
                    choice= input("Select anyone\n1. Erick Musonye\n2. Manju Thapa\n3. Abishkar Tiwari")
                    if choice == "1":
                        print("You have selected a Doctor", choice,"Erick Musonye")
                        take=input("Press enter to go on main menu")
                    elif choice == "2":
                        print("You have selected a Doctor", choice, "Manju Thapa")
                        tool=input("Press enter to go on main menu")
                    elif choice == "3":
                        print("You have selected a Doctor", choice, "Abishkar Tiwari")
                        took=input("Press enter to go on main menu")
                    else:
                        print("Not available")
                        team=input("Press enter to go on main menu")
                if choose == "2":
                    main= input("Press enter to go on main menu")

    if login == "2":
        userName = input("Username\n")
        passWord = input("Password\n")
        print("Successfully Login")
        now = open("demo.txt",'r')
        number= input("Enter PatientID")
        for line in now:
            (patientId, firstName, lastName, address, gender, contact) = line.split()
            if (patientId == number):
                print(patientId, firstName, lastName, address, gender, contact)
        now.close()
        moniter= input("You want to do payment through cash or credit?\n1. Through Cash\n2. Through Credit")
        if moniter == "1":
            keep = input("Enter receipt No.")
            kept = input("Enter total amount")
            now= open("new.txt","a")
            now.write("%16s%16s\n"%(keep,kept))
            now.close()
            print("THANK YOU!!!")
        if moniter == "2":
            work = input("Enter credit card No.")
            wrap = input("Enter total amount")
            now= open("new.txt","a")
            now.write("%16s%16s\n"%(work,wrap))
            now.close()
            print("THANK YOU!!!")

    else:
        print("Wrong option")

must()




