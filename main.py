from validate import *
class Employee:
    empDict={}
    
    def __init__(self,emp_id,emp_name,salary,phone_number,email,age,gender,address,aadharcard,city,dob,department,designation,pan_card,blood_group,marital_status):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.salary=salary
        self.phone_number=phone_number
        self.email=email
        self.age=age
        self.gender=gender
        self.address=address
        self.aadharcard=aadharcard
        self.city=city
        self.dob=dob
        self.department=department
        self.designation=designation
        self.pan_card=pan_card
        self.blood_group=blood_group
        self.marital_status=marital_status
        if self.department in self.empDict.keys():
            self.empDict[self.department].append(self.name)
        else:
            self.empDict[self.department]=[self.name]
       

    def display_empdetails(self):
        print("Employee ID=",self.emp_id)
        print("Employee Name=",self.emp_name)
        print("Salary=",self.salary)
        print("Phone number",self.phone_number)
        print("Email:",self.email)
        print("Age=",self.age)
        print("Gender=",self.gender)
        print("Address=",self.address)
        print("City=",self.city)
        print("Adhar Card=",self.aadharcard)
        print("D.O.B=",self.dob)
        print("Department=",self.department)
        print("Designation=",self.designation)
        print("Pan card=",self.pan_card)
        print("Blood Group=",self.blood_group)
    
    @classmethod
    def departmentWiseDetails(self):
        for k,v in self.empDict.items():
            print(k," = ",v)
empList=[]


while True:
    print("")
    print("1.ADD Details")
    print("2.Display Records")
    print("3.Searching Records")
    print("4.Department wise name of the Employees")
    print("5.Deleting the record ")
    print("6.Updating the record ")
    print("7.Highest salary")
    print("8.Minimum salary")
    print("9. To exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        while True:
            emp_id=input("Enter the employee id: ")
            if validate_empid(emp_id):
                break
            else:
                print("Enter the correct Employee Id!")


        while True:
            emp_name=input("Enter the employee  name : ")
            if validate_name(emp_name):
                break
            else:
                print("Please enter the name correctly")
        while True:
            dob=input("Enter the Date of Birth of the employee: ")
            if validate_dob(dob):
                break
            else:
                print("Enter the correct date of birth.")
        while True:   
            age=input("Enter the age: ")
            if validate_age(age):
                break
            else:
                print("Please enter the correct age")
        while True:    
            gender=input("Enter the gender: ")
            if validate_gender(gender):
                break
            else:
                print("Enter the correct gender")
        while True:
            phone_number=input("Enter the employees Phone Number: ")
            if validate_phone_number(phone_number):
                break
            else:
                print("Enter the correct phone number.")
        while True:
            email=input("Enter email address:")
            if validate_email(email):
                break
            else:
                print("Enter correct email:")
        while True:
            address=input("Enter the employee address: ")
            if validate_address(address):
                break
            else:
                print("Please!!! enter the correct address")
        while True:
            city=input("Enter the city: ")
            if validate_city(city):
                break
            else:
                print("Please!!! enter the coorect city")
        while True:
            salary=input("Enter the salary: ")
            
            
            if validate_salary(salary):
                break
            else:
                print("Enter the salary correctly")
        while True:
            pan_card=input("Enter the employee Pan Card Number: ")
            if validate_PAN(pan_card):
                break
            else:
                print("Enter the pan number correctly")
                
        while True:
            aadharcard=input("Enter the aadhar card number: ")
            if validate_aadhar(aadharcard):
                break
            else:
                print("Enter the aadhar number correctly")
        while True:
            department=input("Enter the department name: ")
            if validate_department(department):
                break
            else:
                print("Enter the department name correctly")
        while True:
            designation=input("Enter the employee's designation: ")
            if validate_designation(designation):
                break
            else:
                print("Enter the designation correctly")
        while True:
            blood_group=input("Enter the blood group:")
            if validate_bloodgroup(blood_group):
                break
            else:
                print("Enter valid blood group:")
        while True:
            marital_status=input("Enter marital status :")
            if validatemarital_status(marital_status):
                break
            else:
                print("Enter a valid choice")
        obj=Employee(emp_id,emp_name,salary,phone_number,email,age,gender,address,aadharcard,city,dob,department,designation,pan_card,blood_group,marital_status)
        empList.append(obj)
        
    elif choice==2:
        for i in empList:
            i.display_empdetails()
    
    elif choice==3:
        while True:
            print("Press A : To search the Employee by the Employee ID")
            print("Press B : To search the employee by their Name")
            print("Press C : To exit the Searching Window")
            ch1=input("Enter the choice: ")
            if ch1=='A':
                p=input("Enter the Employee ID to be searched: ")
                for i in empList:
                    if i.emp_id==p:
                        i.display_empdetails()
            elif ch1=='B':
                p=input("Enter the name of the Employee to be searched: ")
                for i in empList:
                    if i.emp_name==p:
                        i.display_empdetails()
            elif ch1=='C':
                break
    elif choice==4:
        Employee.departmentWiseDetails()
    elif choice==5:
        while True:
            print("Press A : To delete the record by Employee Id")
            print("Press B : To delete the record by Name of the Employee")
            print("Press C : To exit the deletion window")
            ch2=input("Enter your Choice")
            if ch2=='A':
                p=input("Enter the Employee ID")
                for i in empList:
                    if i.emp_id==p:
                        empList.remove(i)
                        print("Employee deleted successfully")
        
            elif ch2=='B':
                p=print("Enter the name of the employee")
                for i in empList:
                    if i.emp_name==p:
                        empList.remove(i)
                        print("Employee deleted sucessfully")
            elif ch2=='C':
                break

    
    elif choice==6:
        
        id_update=input("Enter the Employee ID to update the Records: ")
        for i in empList:
            if i.emp_id == id_update:
                print("Current Records:")
                i.display_empdetails()
                print("")
                print("1: To update the name of the Employee")
                print("2: To update the Date of Birth of the Employee")
                print("3: To update the Address of the Employee")
                print("4: To update the City of the Employee")
                print("5: To update the Salary of the Employee")
                print("6: To exit the update window")
                ch4=int(input("Plase choose the details you want to update: "))
                if ch4==1:
                    emp_name=input("Name = ")
                    i.emp_name=emp_name
                    print("Name updated Successfully")

                elif ch4==2:   
                    dob=int(input("DOB = "))
                    i.dob=dob
                    print("Date of Birth updated Successfully")
               
                elif ch4==3:
                    address=input("Address = ")
                    i.address=address
                    print("Address updated Successfully")
                elif ch4==4:
                    city=input("City = ")
                    i.city=city
                    print("City updated Successfully")
                elif ch4==5:
                    salary=int(input("Salary = "))
                    i.salary=salary
                    print("Salary updated Successfully")
    elif choice==7:
        salist=[]
        for i in empList:
            salist.append(i.salary)
        if len(salist)==0:
            print("Employee list is emplty Please insert employee details ")
            print("")
        else:
            minsal=min(salist)
            print("Employee with min salary:")
            for i in empList:
                
                if i.salary==minsal:
                    i.display_empdetails()
    elif choice==8:
        salist=[]
        for i in empList:
            salist.append(i.salary)
        if len(salist)==0:
            print("Employee list is emplty Please insert employee details ")
            print("")
        else:
            maxsal=max(salist)
            print("Employee with max salary:")
            for i in empList:
                
                if i.salary==maxsal:
                    i.display_empdetails()
            
        
    elif choice==9:
        print("Exiting the Employee Management System. Goodbye!")
        break
    else:
        print("Invalid choice")
    