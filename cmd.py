import os

def cmdver():
    print("cmd.py v0.0.1, open source project.")
    print("github link: ")

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

def cmdthing():
        cmd = input("cmd.py > ")

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