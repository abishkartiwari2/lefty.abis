# patient management system
import time
def confirm(patientId, firstName, lastName, phoneNo, gender, age):
    now = open("demo.txt", 'a')
    now.write("%16s%16s%16s%16s%16s%16s\n" % (patientId, firstName, lastName, phoneNo, gender, age))
    now.close()

def appointment(appointId, patientId, status):
    new = open("new.txt", 'a')
    new.write("%16s%16s%16s\n" % (appointId, patientId, status))
    new.close()

def treatment(treatId, patientId, disease, treatMent):
    next = open("new1.txt", 'a')
    next.write("%16s%16s%16s%16s\n" % (treatId, patientId, disease, treatMent))
    next.close()

def invoice(invoiceId, patientId, treatId, price):
    null = open("new2.txt", 'a')
    null.write("%16s%16s%16s%16f\n" % (invoiceId, patientId, treatId, price))
    null.close()

class MainPart():

    def __init__(self):
        print("PATIENT MANAGEMENT SYSTEM")

    def another(self):
        while True:
            print("LOGIN USER")
            self.address = input("YOUR E-MAIL ADDRESS:")
            if self.address == "lefty.abis@gmail.com".lower():
                self.password = input("YOUR PASSWORD:")
                if self.password == "chelseafbc123".lower():
                    print("Successfully login receptionist account")
                    while True:
                        self.patient = input("MAIN MENU-\n1. REGISTRATION\n2. APPOINTMENT\n3. LOG-OUT")
                        if self.patient == "1":
                            self.patientId = input("PatientId-")
                            self.firstName = input("First Name-")
                            self.lastName = input("Last Name-")
                            self.phoneNo = input("Phone Number-")
                            self.gender = input("Gender-")
                            self.age = input("Age-")
                            confirm(self.patientId, self.firstName, self.lastName, self.phoneNo, self.gender, self.age)
                            print("Register successful")
                        if self.patient == "2":
                            now = open("demo.txt", 'r')
                            self.appointId = input("AppointmentId-")
                            self.number = input("PatientId-")
                            for line in now:
                                (patientId, firstName, lastName, phoneNo, gender, age) = line.split()
                                if (patientId == self.number):
                                    print(patientId, firstName, lastName, phoneNo, gender, age)
                            self.status = input("Status-")
                            appointment(self.appointId, self.patientId, self.status)
                            now.close()
                            print("Appointment Done")

                        if self.patient == "3":
                            print("Returning back to login user")
                            time.sleep(2)
                            break
                    else:
                        print("Invalid password")


            elif self.address == "manjuthapa980@gmail.com".lower():
                self.password = input("YOUR PASSWORD:")
                if self.password == "minuska980".lower():
                    print("Successfully login physican account")
                    while True:
                        self.physic = input("MAIN MENU-\n1. TREATMENT PLAN\n2. LOG-OUT")
                        if self.physic == "1":
                            next = open("demo.txt", 'r')
                            self.treatId = input("TreatmentId-")
                            self.number = input("PatientId-")
                            for line in next:
                                (patientId, firstName, lastName, phoneNo, gender, age) = line.split()
                                if (patientId == self.number):
                                    print(patientId, firstName, lastName, phoneNo, gender, age)
                            self.disease = input("Disease-")
                            self.treatMent = input("Treatment-")
                            treatment(self.treatId, self.patientId, self.disease, self.treatMent)
                            next.close()
                            print("Treatment Done")
                        if self.physic == "2":
                            print("Returning back to login user")
                            time.sleep(2)
                            break
                else:
                    print("Invalid password")

            elif self.address == "lunatich3art@gmail.com".lower():
                self.password = input("YOUR PASSWORD")
                if self.password == "lamjung123".lower():
                    print("Successfully login accountant account")
                    while True:
                        self.account = input("MAIN MENU-\n1. INVOICING\n2. LOG-OUT")
                        if self.account == "1":
                            null = open("demo.txt", 'r')
                            self.invoiceId = input("InoviceId-")
                            self.number = input("PatientId-")
                            for line in null:
                                (patientId, firstName, lastName, phoneNo, gender, age) = line.split()
                                if (patientId == self.number):
                                    print(patientId, firstName, lastName, phoneNo, gender, age)
                            self.treatId = input("TreatmentId-")
                            self.billAmount = input("TOTAL AMOUNT-")
                            self.price = float(self.billAmount)
                            invoice(self.invoiceId, self.patientId, self.treatId, self.price)
                            null.close()
                            print("Invoicing done")
                        if self.account == "2":
                            print("Returning back to login user")
                            time.sleep(2)
                            break
                else:
                    print("Invalid password")
            else:
                print("Invalid e-mail address")



anyObject = MainPart()
anyObject.another()