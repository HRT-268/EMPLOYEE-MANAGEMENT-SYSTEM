import random, string
"""
Generate user ID ✔
add user ✔
list(retrive) user ✔
remove user ✔
update user information✔
"""
def generate_ID():
        user_ID = string.ascii_uppercase + string.digits
        return ''.join(random.choice(user_ID) for i in range(8))

class EditDatabase:
    employeeDatabase = []
    

    def __init__(self, f_name, l_name, age, job_role, employee_ID):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.job_role = job_role
        self.employee_ID = employee_ID


    def add_user(self):
        user_Info = {
            "FIRST NAME": self.f_name,
            "LAST NAME": self.l_name,
            "AGE": self.age,
            "JOB ROLE": self.job_role,
            "EMPLOYEE ID": self.employee_ID
        }
        self.employeeDatabase.append(user_Info)

    def list_current_Users(self):
        if not self.employeeDatabase:
            print("NO EMPLOYEES IN THE SYSTEM\n")
        else:
            print("__________CURRENT EMPLOYEE__________\n")
        for data in self.employeeDatabase:
            for key, value in data.items():
                print(f"{key}: {value}")
            print("\n")

    def remove_user(self, employee_id):
        for user in self.employeeDatabase:
            
            if user["EMPLOYEE ID"] == employee_id:
                self.employeeDatabase.remove(user)
                print(f"Employee with ID {employee_id} removed successfully")
                return
            print(f"No employee with ID {employee_id} found.")
                
   
    def updated_user(self):
        def exitBothLoop():
            raise StopIteration
        try:
            while True:
                checkID = input("Input user ID (press '#' to go to main menu): ")
                if checkID == "#":
                    return
                
                for data in self.employeeDatabase:
                    if  data["EMPLOYEE ID"] == checkID:
                        print(f"User with ID {checkID} found: ")
                        for key, value in data.items():
                            print(f"{key}: {value}")
                        print("\n")

                        while True:
                            print("\nWhat would you like to update:\n1. First name\n2. Last name\n3. Age\n4. Job role\n5. Employee ID\n")
                            edit_update_option = input('Choose an option (i.e "3") or "#" to go to the main menu: ')

                            if edit_update_option == "1":
                                new_fn = input("input new employee first name: ")
                                data["FIRST NAME"] = new_fn.title()
                                print("First Name sucessfully updated")

                            elif edit_update_option == "2":
                                new_ln = input("input new employee last name: ")
                                data["LAST NAME"] = new_ln.title()
                                print("Last Name sucessfully updated")

                            elif edit_update_option == "3":
                                while True:
                                    try:
                                        new_ag = int(input("input new employee age: "))
                                      
                                        if isinstance(new_ag, int):
                                            break
                                    except ValueError:
                                        print("VALUE MUST BE A NUMBER")
                                data["AGE"] = new_ag
                                print("Age sucessfully updated")

                            elif edit_update_option == "4":
                                new_jr = input("input new employee job role: ")
                                data["JOB ROLE"] = new_jr.title()
                                print("New Job role sucessfully updated")

                            elif edit_update_option == "5":
                                new_id = input("input new employee ID: ")
                                data["EMPLOYEE ID"] = new_id
                                print("Employee ID sucessfully updated")
                            elif edit_update_option == "#":
                                exitBothLoop()
                            else:
                                print("INVALID OPTION")
                                continue
                    else:
                        print(f"ID {checkID} not found")
                        continue
        except StopIteration:
            pass
            