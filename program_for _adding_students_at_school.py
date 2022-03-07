

students = [

]
id = 999
while True:
    user_input = input("chose action(C(create) - P(print) - D(delete) - E(exit) - S(save to a file)").upper()#S function does not exists

    if user_input == "C":
        print("ADD NEW STUDENT")
        print("============")
        id += 1#id_number for students starts from 1000
        name = input("give me a name")
        surname = input("give me surname")
        fathersname = input("give me fathers name")
        stop = False

        for i in students:
            if name == i["name"] and surname == i["surname"] and fathersname == i["fathername"]:
                print("already exists ")
                print("Do you wish to continue add elements to it")
                player_input = input("anser(Y/N").upper()
                if player_input == "N":
                    stop = True
                    break
        if stop:
            continue



        age = int(input("give me age"))

        pupip_class = input("give me class")

        id_stu = input("Does she/he have a id?(Y/N)").upper()
        if id_stu == "Y":
            id_number = input("give me id")
        pupil = {}
        pupil["serial code"] = id
        pupil["name"] = name
        pupil["surname"] = surname
        pupil["fathersname"] = fathersname
        pupil["age"] = age
        pupil["pupil class"] = pupip_class

        if id_stu == "Y":
            pupil["id_number"] = id_number
        students.append(pupil)
        print("Assigment was successful")
        print(students[len(students) - 1])

    elif user_input =="P":
        print("PRINT STUDENDS")
        print("===============")

        print(students)
    elif user_input =="D":
        print("DELETE STUDENTS")
        print("===============")
        if students==[]:
            print("There are no students to delete")
            continue
        choise = int(input("choose id to DELETE a student from the list"))
        for p in students:

            if choise == p["serial code"]:
                students.remove(p)
                print("delete was successful you can see it ")
                print("if you type P in terminal")

            else :
                print("Sorry student does not exist")
                break



    elif user_input == "E":
        break

