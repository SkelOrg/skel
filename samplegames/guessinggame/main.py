import random
import secrets
import datetime
import uuid
import math
import os

class skel():
    # Advanced version of print()
    def createLine(text, type="log"):
        if type == "log" or type == "l" or type == 1:
            return print(text)
        elif type == "warning" or type == "warn" or type == "w" or type == 2:
            return print(f"Warning: {text}")
        elif type == "error" or type == "e" or type == 3:
            return print(f"Error: {text}")
        else:
            return print("Invalid parameters.")

    # Function for appending (to), overwriting or creating files
    def editFile(path = None, type = None, text = None):
        if type == "append" or type == "1" or type == "a":
            file = open(path, "a")
            file.write(f"{text}\n")
            file.close()
        elif type == "write" or type == "w" or "2" or type == "overwrite":
            file = open(path, "w")
            file.write(f"{text}")
            file.close()
        elif type == "x" or type == type == "create" or type == "createfile" or type == "3":
            file = open(path, "x")
            file.write(f"{text}")
            file.close()

    # PI value
    pi = 3.141592653589793

    # Make Directory
    def makeDir(path):
        return os.mkdir(path)

    # Remove Directory
    def removeDir(path):
        return os.rmdir(path)

    # List Directory
    def listDir(path):
        return os.listdir(path)

    # Outputs the entirety of a file
    def readFile(path):
        file = open(path, "r")
        filecontents = file.read()
        file.close()
        return filecontents

    # Square Root Calculator
    def squareRoot(num1):
        return math.sqrt(num1)

    # Sin Calculator
    def sin(num1):
        return math.sin(num1)

    # Cos Calculator
    def cos(num1):
        return math.cos(num1)

    # Tan Calculator
    def tan(num1):
        return math.tan(num1)

    # Radian Calculator
    def radians(num1):
        return math.radians(num1)

    # Degrees Calculator
    def degrees(num1):
        return math.degrees(skel.pi/num1)

    # Euler (e) value
    def Euler():
        return math.e

    # PI function
    def PI():
        return math.pi

    # Time
    def getTime():
        ctime = datetime.datetime.now()
        return print(f"The time is {ctime.strftime('%y/%m/%d %H:%M')}")

    # Random Number Generator
    def randNum(num1, num2):
        return random.randint(num1, num2)

    # Number Formatter
    def formatNum(num=1000, printResult=True):
        formattednumber = "{:,}".format(num)
        if printResult == True:
            print(formattednumber)
        elif printResult == False:
            return formattednumber
        else:
            return print("The 'printResult' parameter is invalid.")

    # Gets a random item from an array
    def randItem(arrayname):
        return random.choice(arrayname)

    # Randomized Key Generator
    def generateKey(type="uuid4", numOfChars=12):
        if type == "uuid4" or type == 4:
            return print(f"UUID4: {str(uuid.uuid4())}")
        elif type == "hextoken":
            return print(secrets.token_hex(numOfChars))
        else:
            return print("The 'type' parameter given is invalid.")

    # Mathmatical operator (4 operations)
    def calculate(num1 = 9, operation = "add", num2 = 3, printresult = True):
        # Multiply operator (x or *)
        if operation == "x" or operation == "*" or operation == "X" or operation == "times" or operation == "times by" or operation == "multiplied by":
            if printresult == True:
                return print(num1 * num2)
            elif printresult == False:
                return num1 * num2
            else:
                print(f"You didn't specify 'True' or 'False'. Your given parameter was '{printresult}'.")

        # Subtract operator (-)
        elif operation == "takeaway" or operation == "take away" or operation == "minus" or operation == "-" or operation == "subtracted by":
            if printresult == True:
                return print(num1 - num2)
            elif printresult == False:
                return num1 - num2
            else:
                print(f"You didn't specify 'True' or 'False'. Your given parameter was '{printresult}'.")

        # Division operator (÷)
        elif operation == "divided by" or operation == "÷" or operation == "//":
            if printresult == True:
                return print(num1 // num2)
            elif printresult == False:
                return num1 // num2
            else:
                print(f"You didn't specify 'True' or 'False'. Your given parameter was '{printresult}'.")

        # Addition operator (+)
        elif operation == "plus" or operation == "+" or operation == "add":
            if printresult == True:
                return print(num1 + num2)
            elif printresult == False:
                return num1 + num2
            else:
                print(f"You didn't specify 'True' or 'False'. Your given parameter was '{printresult}'.")

        else:
            print(f"That isn't an operation. Your given operation was '{operation}'.")

    # Request user to input anything
    def requestUserInput(text = None):
        return input(text)
