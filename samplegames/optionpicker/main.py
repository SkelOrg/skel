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
        if type == "append" or "1" or "a":
            file = open(path, "a")
            file.write(f"{text}\n)
            file.close()
        elif type == "write" or "w" or "2" or "overwrite":
            file = open(path, "w")
            file.write(f"{text})
            file.close()
        elif type == "x" or "create" or "createfile" or "3":
            file = open(path, "x")
            file.write(f"{text})
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

    # Addition Operator (+)
    def add(num1 = 9, num2 = 3):
        return print(num1 + num2)

    # Addition Operator (-)
    def subtract(num1 = 9, num2 = 3):
        return print(num1 - num2)

    # Multiplication Operator (x)
    def multiply(num1 = 9, num2 = 3):
        return print(num1 * num2)

    # Division Operator (÷)
    def divide(num1 = 9, num2 = 3):
        return print(num1 // num2)

    # Request user to input anything
    def requestUserInput(text = None):
        return input(text)
