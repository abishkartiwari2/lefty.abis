print("PATIENT MANAGEMENT SYSTEM")

def login():
    print("LOGIN HERE")
    username = input("Username:")
    password = input("Password:")
login()

reg_file = "demo.txt"

def confirm(patientId, firstName, lastName, phoneNo, gender, dateBirth):
    now = open(reg_file, 'a')
    now.write("%16s%16s%16s%16s%16s%16s\n" % (patientId, firstName, lastName, phoneNo, gender, dateBirth))
    now.close()


app_file = "new.txt"

def appointment(appointId, patientId, status):
    new = open(app_file, 'a')
    new.write("%16s%16s%16s\n" % (appointId, patientId, status))
    new.close()


tre_file = "new1.txt"

def treatment(treatId, patientId, disease, treatMent):
    next = open(tre_file, 'a')
    next.write("%16s%16s%16s%16s\n" % (treatId, patientId, disease, treatMent))
    next.close()


inv_file = "new2.txt"

def invoice(invoiceId, patientId, treatId, price):
    null = open(inv_file, 'a')
    null.write("%16s%16s%16s%16f\n" % (invoiceId, patientId, treatId, price))
    null.close()

def home():
    while True:
        print("Choose your option?")
        option = input("1. RECEPTION\n2. PHYSICIAN\n3. ACCOUNTANT")

        def reception():
            if option == "1":
                while True:
                    print("Choose your option?")
                    patient = input("1. REGISTRATION\n2. APPOINTMENT\n3. QUIT")
                    if patient == "1":
                        patientId = input("PatientId-")
                        firstName = input("First Name-")
                        lastName = input("Last Name-")
                        phoneNo = input("Phone Number-")
                        gender = input("Gender-")
                        dateBirth = input("DOB-")
                        confirm(patientId, firstName, lastName, phoneNo, gender, dateBirth)
                        print("Register successful")
                    if patient == "2":
                        now = open(reg_file, 'r')
                        appointId = input("AppointmentId-")
                        number = input("PatientId-")
                        for line in now:
                            (patientId, firstName, lastName, phoneNo, gender, dateBirth) = line.split()
                            if (patientId == number):
                                print(patientId, firstName, lastName, phoneNo, gender, dateBirth)
                        status = input("Status-")
                        appointment(appointId, patientId, status)
                        now.close()
                        print("Appointment Done")

                    if patient == "3":
                        print()
                        break

            if option == "2":
                print("Choose your option?")
                while True:
                    physic = input("1. TREATMENT PLAN\n2. QUIT")
                    if physic == "1":
                        next = open(reg_file, 'r')
                        treatId = input("TreatmentId-")
                        number = input("PatientId-")
                        for line in next:
                            (patientId, firstName, lastName, phoneNo, gender, dateBirth) = line.split()
                            if (patientId == number):
                                print(patientId, firstName, lastName, phoneNo, gender, dateBirth)
                        disease = input("Disease-")
                        treatMent = input("Treatment-")
                        treatment(treatId, patientId, disease, treatMent)
                        next.close()
                        print("Treatment Done")
                    if physic == "2":
                        print("")
                        break
            if option == "3":
                print("Choose your option?")
                while True:
                    account = input("1. INVOICING\n2. QUIT")
                    if account == "1":
                        null = open(reg_file, 'r')
                        invoiceId = input("InoviceId-")
                        number = input("PatientId-")
                        for line in null:
                            (patientId, firstName, lastName, phoneNo, gender, dateBirth) = line.split()
                            if (patientId == number):
                                print(patientId, firstName, lastName, phoneNo, gender, dateBirth)
                        treatId = input("TreatmentId-")
                        billAmount = input("TOTAL AMOUNT-")
                        price = float(billAmount)
                        invoice(invoiceId, patientId, treatId, price)
                        null.close()
                        print("Invoicing done")
                    if account == "2":
                        print("")
                        break

        reception()
home()






