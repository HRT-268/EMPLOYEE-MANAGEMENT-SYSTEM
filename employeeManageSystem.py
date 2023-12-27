import managementSystem
print("___________WELCOME TO VALANINE CO MANAGEMENT SYSTEM____________\n")

while True:
    try:
        print("\nWould you like to:\n1. Generate new user ID\n2. Add employee\n3. List current employees\n4. Remove employee\n5. Update employee details\n")
        edit_option = input('Choose an option (i.e 3 or press "#" to exit the program): ')
        NewUser_ID = managementSystem.generate_ID()


        if edit_option == "1":
            print(f"New employee ID: {NewUser_ID}")


        elif edit_option == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            while True:
                try:
                    age = int(input("Enter age: ")) #Catch error when string or other value type is entered
                    if isinstance(age, int):
                        break
                except ValueError:
                    print("VALUE MUST BE A NUMBER")
                

            job_role = input("Enter job role: ")
            employee_id = input("Enter employee ID: ")
            obj2 = managementSystem.EditDatabase(first_name.title(), last_name.title(), age, job_role.title(), employee_id)
            obj2.add_user()

        elif edit_option == "3":
            obj3 = managementSystem.EditDatabase("", "", "", "", "")
            obj3.list_current_Users()

        elif edit_option == "4":
            remove_employee = input("Input employee ID: ")
            obj4 = managementSystem.EditDatabase("", "", "", "", "")
            obj4.remove_user(remove_employee)
            
        # I do not understand this block of code
        elif edit_option == "5":
            obj5 = managementSystem.EditDatabase("", "", "", "", "")
            if obj5.updated_user():
                break

        elif edit_option == "#": 
            break
        else:
            print("Ivalid value...Going back up!!!")
            continue

    except KeyboardInterrupt:
        print("KeyboardInterrupt caught, but continuing execution.")
        continue