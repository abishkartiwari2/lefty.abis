# patient management system
import time
def confirm(patientId, firstName, lastName, phoneNo, gender, age):
    now = open("demo.txt", 'a')
    now.write("%16s%16s%16s%16s%16s%16s\n" % (patientId, firstName, lastName, phoneNo, gender, age))
    now.close()

def appointment(appointId, status):
    new = open("new.txt", 'a')
    new.write("%16s%16s\n" % (appointId, status))
    new.close()

def treatment(treatId, disease, treatMent):
    next = open("new1.txt", 'a')
    next.write("%16s%16s%16s\n" % (treatId, disease, treatMent))
    next.close()

def invoice(invoiceId, treatId, price):
    null = open("new2.txt", 'a')
    null.write("%16s%16s%16f\n" % (invoiceId, treatId, price))
    null.close()

def bill(receiptNo):
    null = open("new2.txt",'a')
    null.write("%16s\n"%(receiptNo))
    null.close()

def credit(creditNo):
    null = open("new2.txt",'a')
    null.write("%0s\n"%(creditNo))
    null.close()

def file(address,password):
    file = open("new0.txt", 'r')
    file.write("%16s%16s\n" % (address,password))
    file.close()



class MainPart():

    def __init__(self):
        print(" ")
    def another(self):
        while True:
            print("Patient Management System  for PRUDENT HEALTHCARE")
            print("LOGIN PORTAL")
            file = open("new0.txt",'r')
            self.address = input("YOUR E-MAIL ADDRESS:")
            if self.address == "admin":
                self.password = input("YOUR PASSWORD:")
                if self.password == "admin1":
                    for line in file:
                        (address,password)= line.split()
                        if (password == self.password):
                            time.sleep(2)
                            print("Successfully login RECEPTIONIST ACCOUNT")
                            while True:
                                self.patient = input("RECEPTIONIST MAIN MENU-\n1. REGISTRATION\n2. APPOINTMENT\n3. LOG-OUT")
                                if self.patient == "1":
                                    self.patientId = input("PatientId-")
                                    self.firstName = input("First Name-")
                                    self.lastName = input("Last Name-")
                                    self.phoneNo = input("Phone Number-")
                                    self.gender = input("Gender-")
                                    self.age = input("Age-")
                                    confirm(self.patientId, self.firstName, self.lastName, self.phoneNo, self.gender, self.age)
                                    print("Registered new patient and info. saved in textfile")
                                    print("Returning back to RECEPTIONIST MAIN-MENU")
                                    time.sleep(2)

                                if self.patient == "2":
                                    self.appointId = input("AppointmentId-")
                                    self.status = input("Status-")
                                    appointment(self.appointId, self.status)
                                    print("Successfully appointed and info. saved in textfile")
                                    print("Returning back to RECEPTIONIST MAIN-MENU")
                                    time.sleep(2)

                                if self.patient == "3":
                                        print("Returning back to LOGIN PORTAL")
                                        time.sleep(2)
                                        break
                else:
                    print("Enter valid password")

            elif self.address == "admin":
                self.password = input("YOUR PASSWORD:")
                if self.password == "admin2":
                    for line in file:
                        (address, password) = line.split()
                        if (address == self.address):
                            time.sleep(2)
                            print("Successfully login PHYSICIAN ACCOUNT")
                            while True:
                                self.physic = input("PHYSICIAN MAIN MENU-\n1. TREATMENT PLAN\n2. LOG-OUT")
                                if self.physic == "1":
                                    self.treatId = input("TreatmentId-")
                                    self.disease = input("Disease-")
                                    self.treatMent = input("Treatment-")
                                    treatment(self.treatId, self.disease, self.treatMent)
                                    print("Treatment Done and info. saved in textfile")
                                    print("Returning back to PHYSICIAN MAIN-MENU")
                                    time.sleep(2)
                                if self.physic == "2":
                                    print("Returning back to LOGIN PORTAL")
                                    time.sleep(2)
                                    break
                else:
                    print("Enter valid password")

            elif self.address == "admin":
                self.password = input("YOUR PASSWORD")
                if self.password == "admin3":
                    for line in file:
                        (address, password) = line.split()
                        if (address == self.address):
                            time.sleep(2)
                            print("Successfully login ACCOUNTANT ACCOUNT")
                            while True:
                                self.account = input("ACCOUNTANT MAIN MENU-\n1. INVOICING\n2. SEARCH PATIENT\n3. RECEIPT PAYMENT \n4. LOG-OUT")
                                if self.account == "1":
                                    self.invoiceId = input("InoviceId-")
                                    self.treatId = input("TreatmentId-")
                                    self.billAmount = input("TOTAL AMOUNT-")
                                    self.price = float(self.billAmount)
                                    invoice(self.invoiceId, self.treatId, self.price)
                                    print("Invoicing done and info. saved in textfile")
                                    print("Returning back to ACCOUNTANT MAIN-MENU")
                                    time.sleep(2)
                                if self.account == "2":
                                    while True:
                                            try:
                                                now = open("demo.txt", "r")
                                                number = input("PatientID")
                                                for line in now:
                                                    (patientId, firstName, lastName, phoneNo, gender, age) = line.split()
                                                    if (patientId == number):
                                                        print(patientId, firstName, lastName, phoneNo, gender, age)
                                                        print("PatientId exist")
                                                        print("Returning back to ACCOUNTANT MAIN-MENU")
                                                        time.sleep(2)
                                                        break
                                                else:
                                                    print("PatientId doesn't exist")
                                                    print("Returning back to ACCOUNTANT MAIN-MENU")
                                                    time.sleep(2)

                                            except:
                                                print("PatientId doesn't exist")
                                                now.close()
                                            break

                                if self.account == "3":
                                    self.receiptAmount = input("Choose you option?\n1. Cash Receipt \n2. Credit Card \n")
                                    if self.receiptAmount == "1":
                                        self.receiptNo = input("Enter Cash Receipt No.-")
                                        bill(self.receiptNo)
                                        print("Info. saved in database")
                                        print("Returning back to ACCOUNTANT MAIN-MENU")
                                        time.sleep(2)
                                    if self.receiptAmount == "2":
                                        self.creditNo = input("Enter Credit Card No.-")
                                        credit(self.creditNo)
                                        print("Info. saved in database")
                                        print("Returning back to ACCOUNTANT MAIN-MENU")
                                        time.sleep(2)
                                if self.account == "4":
                                    print("Returning back to LOGIN PORTAL")
                                    time.sleep(2)
                                    break

                else:
                    print("Enter valid password")

            else:
                print("Invalid e-mail address")

anyObject = MainPart()
anyObject.another()
