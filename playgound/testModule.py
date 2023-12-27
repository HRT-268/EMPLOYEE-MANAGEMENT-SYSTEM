class test:
    sample_list = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sample_add(self):
        user = {
            "NAME": self.name,
            "AGE": self.age
        }
        self.sample_list.append(user)

    def sampleList(self):
        if not self.sample_list:
            print("NO EMPLOYEES IN THE SYSTEM\n")
        else:
            print("__________CURRENT EMPLOYEE__________\n")
        for data in self.sample_list:
            for key, value in data.items():
                print(f"{key}: {value}")
            print("\n")

    def sample_update(self):
        def exitBothLoop():
            raise StopIteration
        try:
            while True:
                newInputs = input("INput age press 'q' to go to main menu: ")
                if newInputs == 'q':
                    return
                    
                
                for data in self.sample_list:
                        
                        if data["AGE"] == newInputs: 
                            for key, value in data.items():
                                    print(f"{key}: {value}")
                            print("\n")

                            while True:
                                updateDetails = input("1 to update name and 2 to update Age. press 3 to go to main menu: ")
                                
                                if updateDetails == "1":
                                    newName = input("Input new name: ")
                                    data["NAME"] = newName
                                    print("Name successfully updated")
                                    continue
                                elif updateDetails == "2":
                                    newAge = input("Input new age: ")
                                    data["AGE"] = newAge
                                    print("Age successfully updated")
                                    continue
                                elif updateDetails == "3":
                                    exitBothLoop() 
                
                                else:
                                    print("Invalid option")
                                    continue
                                
                        else:
                            print("age not found")
                            continue
        except StopIteration:
            pass
            