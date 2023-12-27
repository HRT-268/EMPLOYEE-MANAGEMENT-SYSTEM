import testModule



while True:
    sampleUser = input("Input 1 for add, press 2 for listing, and 3 for update: ")
    if sampleUser == "1":
        name = input("Input name: ")
        age = input("input age: ")
        obj1 = testModule.test(name, age)
        obj1.sample_add()
        

    elif sampleUser == "2":
        obj2 = testModule.test("", "")
        obj2.sampleList()
    elif sampleUser == "3":
        obj3 = testModule.test("", "")

        if obj3.sample_update():
            break
        
    else:
        break
    