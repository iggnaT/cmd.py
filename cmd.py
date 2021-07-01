import os

def say(thing):
    print(thing)

def cmdver():
    print("cmd.py v0.0.2, open source project.")
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

def cmdthing():
        cmd = input("cmd.py > ")

        if(cmd == "cmd.py"):
            cmdver()
        if(cmd == "cmd"):
            cmdver()
        if(cmd == "ver"):
            cmdver()

        if(cmd == "say"):
            say(input("what to say: "))

        if(cmd == ""):
            cmdthing()
        try:
            if(cmd == "math"):
                math(int(input("number 1: ")), input("what to do (+, -, * or /): "), int(input("number 2: ")))
        except:
            print("error 5: some input fields are incorrect")
            
        if(cmd == "\n"):
            cmdthing()

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
