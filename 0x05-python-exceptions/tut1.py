#!/usr/bin/python3
try:
    args = [1,2,3]

    print(args[3])

except IndexError:
    print("Error: Index doesn't exist")

except:
    print("Unknown Error")
