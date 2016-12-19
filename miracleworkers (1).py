# patient management system
import time
def confirm(patientId, firstName, lastName, phoneNo, gender, age):
    now = open("demo.txt", 'a')
    now.write("%16s%16s%16s%16s%16s%16s\n" % (patientId, firstName, lastName, phoneNo, gender, age))
    now.close()

def appointment(appointId, number, status):
    new = open("new.txt", 'a')
    new.write("%16s%16s%16s\n" % (appointId, number, status))
    new.close()

def treatment(treatId, number, disease, treatMent):
    next = open("new1.txt", 'a')
    next.write("%16s%16s%16s%16s\n" % (treatId, number, disease, treatMent))
    next.close()

def invoice(invoiceId, number, treatId, price):
    null = open("new2.txt", 'a')
    null.write("%16s%16s%16s%16f\n" % (invoiceId, number, treatId, price))
    null.close()

def file(address,password):
    file = open("new0.txt", 'r')
    file.write("%16s%16s\n" % (address,password))
    file.close()



class MainPart():

    def __init__(self):
        print("Patient Management System  for PRUDENT HEALTHCARE")
    def another(self):
        while True:
            print("LOGIN USER")
            file = open("new0.txt",'r')
            self.address = input("YOUR E-MAIL ADDRESS:")
            if self.address == "lefty.abis@gmail.com":
                self.password = input("YOUR PASSWORD:")
                if self.password == "chelseafbc123":
                    for line in file:
                        (address,password)= line.split()
                        if (password == self.password):
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
                                    print("Successfully registered and info. saved in textfile")
                                    print("Returning back to RECEPTIONIST MAIN-MENU")
                                    time.sleep(2)
                                if self.patient == "2":
                                    self.appointId = input("AppointmentId-")
                                    now = open("demo.txt", 'r')
                                    self.number = input("PatientId-")
                                    for line in now:
                                        (patientId, firstName, lastName, phoneNo, gender, age) = line.split()
                                        if (patientId == self.number):
                                            print(patientId, firstName, lastName, phoneNo, gender, age)
                                    now.close()
                                    self.status = input("Status-")
                                    appointment(self.appointId, self.number, self.status)
                                    print("Successfully appointed and info. saved in textfile")
                                    print("Returning back to RECEPTIONIST MAIN-MENU")
                                    time.sleep(2)
                                if self.patient == "3":
                                    print("Returning back to LOGIN PORTAL")
                                    time.sleep(2)
                                    break

            if self.address == "manjuthapa980@gmail.com":
                self.password = input("YOUR PASSWORD:")
                if self.password == "minuska980":
                    for line in file:
                        (address, password) = line.split()
                        if (address == self.address):
                            print("Successfully login PHYSICIAN ACCOUNT")
                            while True:
                                self.physic = input("PHYSICIAN MAIN MENU-\n1. TREATMENT PLAN\n2. LOG-OUT")
                                if self.physic == "1":
                                    self.treatId = input("TreatmentId-")
                                    now = open("demo.txt",'r')
                                    self.number = input("PatientId-")
                                    for line in now:
                                        (patientId, firstName, lastName, phoneNo, gender, age) = line.split()
                                        if (patientId == self.number):
                                            print(patientId, firstName, lastName, phoneNo, gender, age)
                                    now.close()
                                    self.disease = input("Disease-")
                                    self.treatMent = input("Treatment-")
                                    treatment(self.treatId, self.number, self.disease, self.treatMent)
                                    print("Treatment Done and info. saved in textfile")
                                    print("Returning back to PHYSICIAN MAIN-MENU")
                                    time.sleep(2)
                                if self.physic == "2":
                                    print("Returning back to LOGIN PORTAL")
                                    time.sleep(2)
                                    break


            if self.address == "lunatich3art@gmail.com":
                self.password = input("YOUR PASSWORD:")
                if self.password == "lamjung123":
                    for line in file:
                        (address, password) = line.split()
                        if (password == self.password):
                            print("Successfully login ACCOUNTANT ACCOUNT")
                            while True:
                                self.account = input("ACCOUTANT MAIN MENU-\n1. INVOICING\n2. LOG-OUT")
                                if self.account == "1":
                                    self.invoiceId = input("InoviceId-")
                                    now = open("demo.txt", 'r')
                                    self.number = input("PatientId-")
                                    for line in now:
                                        (patientId, firstName, lastName, phoneNo, gender, age) = line.split()
                                        if (patientId == self.number):
                                            print(patientId, firstName, lastName, phoneNo, gender, age)
                                    now.close()
                                    self.treatId = input("TreatmentId-")
                                    self.billAmount = input("TOTAL AMOUNT-")
                                    self.price = float(self.billAmount)
                                    invoice(self.invoiceId, self.number, self.treatId, self.price)
                                    print("Invoicing done and all info. saved in textfile")
                                    print("Returning back to ACCOUNTANT MAIN-MENU")
                                    time.sleep(2)
                                if self.account == "2":
                                    print("Returning back to LOGIN PORTAL")
                                    time.sleep(2)
                                    break
            else:
                print("Invalid e-mail address or password ")

anyObject = MainPart()
anyObject.another()