print ("Welcome to system")

loop = True
count1 = 0
count2 = 0
while loop:
    username = input("Username: ")
    if username == "dinhtien":
        while loop:
            password = input("Password: ")
            if password == 1202:
                print("Login successfull!")
                break
            else:
                if count1 >= 2:
                    print("get away")
                    break
                else:
                    count1 += 1
                    print("Password is wrong, try again!")
    else:
        if count2 >= 2:
            print("get away")
            break
        else:
            count2 += 1
            print("Username is wrong, try again!")
