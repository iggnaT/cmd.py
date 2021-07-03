import os

path = os.path.join("C:\\Users\\Public\\cmd.py\\config\\", "config.cfg")

def firstenter():
    try:
        os.mkdir("C:\\Users\\Public\\cmd.py")
        os.mkdir("C:\\Users\\Public\\cmd.py\\config")
        name = input("hi there! what's your name (you will be able to change it any time): ")
        password = input("password (if this field will be blank then you will have only to press enter when your password is asked): ")
        f = open(path, 'w')
        f.write(name)
        f.write("," + password)
        f.close
    except:
        pass

firstenter()

def getname():
    f = open(path, 'r')
    data = f.read().split(",", 1)
    return data[0]

def getpassword():
    f = open(path, 'r')
    data = f.read().split(",", 1)
    return data[1]

globalpassword = getpassword()
globalname = getname()

def checkpassword(userpassword):
    if(userpassword == getpassword()):
        return True
    else:
        return False

def say(thing):
    print(thing)

def changename():
    newname = input("what name do you want: ")
    f = open(path, 'w')
    f.write(newname + "," + globalpassword)
    f.close
    globalname = newname

def changepassword():
    globalname = getname()
    newpass = input("enter new password: ")
    globalname = getname()
    f = open(path, 'w')
    f.write(globalname + "," + newpass)
    f.close
    globalname = getname()

def whatsnew():
    print("added:")
    print("password system")
    print("new command chngpass")

def cmdver():
    print("cmd.py v0.0.4, open source project.")
    print("github link: https://github.com/iggnaT/cmd.py")
    print("check it often for new updates")
    print("type help to get help")

cmdver()

def math(number1, char, number2):
    if(char == "+"):
        print(number1 + number2)
    
    if(char == "-"):
        print(number1 - number2)

    if(char == "*"):
        print(number1 * number2)

    if(char == "/"):
        print(number1 / number2)

def readfile(filename):
    x = open(filename, 'r')
    print(x.read())

def delete(filename):
    if os.path.exists(filename):
          os.remove(filename)
    else:
          print("error 14: file does not exist, please check if you misspelled it.")    

def create(filename, content): 
    with open(filename, 'w') as fp:
        fp.write(content)

def help(): # todo: add more help xd
    print("exit - exits cmd.py")
    print("help - shows help menu")
    print("crt - creates file") # did: make create() work
    print("dlt - deletes file")
    print("read - reads file")
    print("math - simple calculator")
    print("ver - shows version")
    print("say - says what you type")
    print("chngname - changes name you specified on first launch of cmd.py")
    print("chngpass - changes password")
    print("whnew - shows what has been added and what was removed")

def cmdthing():
        firstenter()
        globalname = getname()

        cmd = input("cmd.py\\" + globalname + " > ")

        if(cmd == "cmd.py"):
            cmdver()
        if(cmd == "cmd"):
            cmdver()
        if(cmd == "ver"):
            cmdver()

        if(cmd == "whoami"):
            print(name)
            cmdthing()

        if(cmd == "say"):
            say(input("what to say: "))
            cmdthing()

        if(cmd == "whnew"):
            whatsnew()
            cmdthing()

        if(cmd == ""):
            cmdthing()

        try:
            if(cmd == "math"):
                math(int(input("number 1: ")), input("what to do (+, -, * or /): "), int(input("number 2: ")))
                cmdthing()
        except:
            print("error 5: some input fields are incorrect")
            cmdthing()
            
        if(cmd == "\n"):
            cmdthing()

        elif(cmd == "chngpass"):
            abletodo = checkpassword(input("enter old password: "))
            if(abletodo == True):
                changepassword()
                cmdthing()
            else:
                print("wrong password. try again. you have one attempt left")
                abletodo = checkpassword(input("enter old password: "))
                if(abletodo == True):
                    changepassword()()
                    cmdthing()
                else:
                    print("wrong password. try again later")
                    cmdthing()

        elif(cmd == "chngname"):
            abletodo = checkpassword(input("password: "))
            if(abletodo == True):
                changename()
                cmdthing()
            else:
                print("wrong password. try again. you have one attempt left")
                abletodo = checkpassword(input("password: "))
                if(abletodo == True):
                    changename()
                    cmdthing()
                else:
                    print("wrong password. try again later")
                    cmdthing()
                
        elif(cmd == "read"):
            readfile(input("file name: "))     
            cmdthing()       

        elif(cmd == " "):
            cmdthing()

        elif(cmd == "exit"):
            exit()

        elif(cmd == "crt"):
            abletodo = checkpassword(input("password: "))
            if(abletodo == True):
                create(input("file name: "), input("contents: "))
                cmdthing()
            else:
                print("wrong password. try again. you have one attempt left")
                abletodo = checkpassword(input("password: "))
                if(abletodo == True):
                    create(input("file name: "), input("contents: "))
                    cmdthing()
                else:
                    print("wrong password. try again later")
                    cmdthing()

        elif(cmd == "dlt"):
            abletodo = checkpassword(input("password: "))
            if(abletodo == True):
                delete(input("file name: "))
                cmdthing()
            else:
                print("wrong password. try again. you have one attempt left")
                abletodo = checkpassword(input("password: "))
                if(abletodo == True):
                    delete(input("file name: "))
                    cmdthing()
                else:
                    print("wrong password. try again later")
                    cmdthing()

        elif(cmd == "help"):
            help()
            cmdthing()

        else:
            print("wrong command. type help for help")
            cmdthing()

while True:
    cmdthing()
