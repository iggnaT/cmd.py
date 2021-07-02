import os

name = "user"
path = os.path.join("C:\\Users\\Public\\cmd.py\\config\\", "config.cfg")

def firstenter():
    try:
        os.mkdir("C:\\Users\\Public\\cmd.py")
        os.mkdir("C:\\Users\\Public\\cmd.py\\config")
        name = input("hi there! what's your name (you will be able to change it any time): ")
        f = open(path, 'w')
        f.write(name)
        f.close
    except:
        pass

def getname():
    f = open("C:\\Users\\Public\\cmd.py\\config\\config.cfg", 'r')
    return f.read()

def say(thing):
    print(thing)

def changename():
    newname = input("what name do you want: ")
    f = open(path, 'w')
    f.write(newname)
    f.close

def whatsnew():
    print("added:")
    print("user system")
    print("whats new command")

def cmdver():
    print("cmd.py v0.0.3, open source project.")
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
    print("whnew - shows what has been added and what was removed")

def cmdthing():
        firstenter()
        name = getname()

        cmd = input("cmd.py\\" + name + " > ")

        if(cmd == "cmd.py"):
            cmdver()
        if(cmd == "cmd"):
            cmdver()
        if(cmd == "ver"):
            cmdver()

        if(cmd == "say"):
            say(input("what to say: "))

        if(cmd == "whnew"):
            whatsnew()

        if(cmd == ""):
            cmdthing()

        try:
            if(cmd == "math"):
                math(int(input("number 1: ")), input("what to do (+, -, * or /): "), int(input("number 2: ")))
        except:
            print("error 5: some input fields are incorrect")
            
        if(cmd == "\n"):
            cmdthing()

        elif(cmd == "chngname"):
            changename()

        elif(cmd == "read"):
            readfile(input("file name: "))            

        elif(cmd == " "):
            cmdthing()

        elif(cmd == "exit"):
            exit()

        elif(cmd == "crt"):
            create(input("file name: "), input("contents: "))

        elif(cmd == "dlt"):
            delete(input("file name: "))

        elif(cmd == "help"):
            help()

        else:
            print("wrong command. type help for help")

while True:
    cmdthing()
