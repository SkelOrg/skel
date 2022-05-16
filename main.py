from random import randint, choice
from secret import token_hex
from datetime import datetime
from uuid import uuid4
from math import sin, cos, tan, degrees, radians, e, pi, sqrt
from os import listdir, mkdir, rmdir
from sys import stdin, stdout

class skel():
    # Advanced version of print()
    def createLine(text, type="log"):
        if type == "log" or type == "l" or type == 1:
            return stdout.write(text + "\n")
        elif type == "warning" or type == "warn" or type == "w" or type == 2:
            return stdout.write(f"Warning: {text}\n")
        elif type == "error" or type == "e" or type == 3:
            return stdout.write(f"Error: {text}\n")
        else:
            return stdout.write("Invalid parameters.\n")

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
        return mkdir(path)

    # Remove Directory
    def removeDir(path):
        return rmdir(path)

    # List Directory
    def listDir(path):
        return listdir(path)

    # Outputs the entirety of a file
    def readFile(path):
        file = open(path, "r")
        filecontents = file.read()
        file.close()
        return filecontents

    # Square Root Calculator
    def squareRoot(num1):
        return sqrt(num1)

    # Sin Calculator
    def sin(num1):
        return sin(num1)

    # Cos Calculator
    def cos(num1):
        return cos(num1)

    # Tan Calculator
    def tan(num1):
        return tan(num1)

    # Radian Calculator
    def radians(num1):
        return radians(num1)

    # Degrees Calculator
    def degrees(num1):
        return degrees(skel.pi/num1)

    # Euler (e) value
    def Euler():
        return e

    # PI function
    def PI():
        return pi

    # Time
    def getTime():
        ctime = datetime.now()
        return stdout.write(f"The time is {ctime.strftime('%y/%m/%d %H:%M')}\n")

    # Random Number Generator
    def randNum(num1, num2):
        return randint(num1, num2)

    # Number Formatter
    def formatNum(num=1000, printResult=True):
        formattednumber = "{:,}".format(num)
        if printResult == True:
            stdout.write(formattednumber + "\n")
        elif printResult == False:
            return formattednumber
        else:
            return stdout.write("The 'printResult' parameter is invalid.\n")

    # Gets a random item from an array
    def randItem(arrayname):
        return choice(arrayname)

    # Randomized Key Generator
    def generateKey(type="uuid4", numOfChars=12):
        if type == "uuid4" or type == 4:
            return stdout.write(f"UUID4: {str(uuid4())}\n")
        elif type == "hextoken":
            return stdout.write(token_hex(numOfChars) + "\n")
        else:
            return stdout.write("The 'type' parameter given is invalid.\n")

    # Mathmatical operator (4 operations)
    def calculate(num1 = 9, operation = "add", num2 = 3, printresult = True):
        # Multiply operator (x or *)
        if operation == "x" or operation == "*" or operation == "X" or operation == "times" or operation == "times by" or operation == "multiplied by":
            if printresult == True:
                return stdout.write(num1 * num2 + "\n")
            elif printresult == False:
                return num1 * num2
            else:
                stdout.write(f"You didn't specify 'True' or 'False'. Your given parameter was '{printresult}'.\n")

        # Subtract operator (-)
        elif operation == "takeaway" or operation == "take away" or operation == "minus" or operation == "-" or operation == "subtracted by":
            if printresult == True:
                return stdout.write(num1 - num2 + "\n")
            elif printresult == False:
                return num1 - num2
            else:
                stdout.write(f"You didn't specify 'True' or 'False'. Your given parameter was '{printresult}'.\n")

        # Division operator (÷)
        elif operation == "divided by" or operation == "÷" or operation == "//":
            if printresult == True:
                return stdout.write(num1 // num2 + "\n")
            elif printresult == False:
                return num1 // num2
            else:
                stdout.write(f"You didn't specify 'True' or 'False'. Your given parameter was '{printresult}'.\n")

        # Addition operator (+)
        elif operation == "plus" or operation == "+" or operation == "add":
            if printresult == True:
                return stdout.write(num1 + num2 + "\n")
            elif printresult == False:
                return num1 + num2
            else:
                stdout.write(f"You didn't specify 'True' or 'False'. Your given parameter was '{printresult}'.\n")

        else:
            stdout.write(f"That isn't an operation. Your given operation was '{operation}'.\n")

    # Request user to input anything
    def requestUserInput(text = None):
        stdout.write(text)
        stdout.flush()
        return stdin.readline()
