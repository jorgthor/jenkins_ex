#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the main file for the project
"""
import functions

def main(*args):
    """
    If no arguments are passed, the user is prompted to enter the numbers and the operation they want to perform.
    :param args[0]: The operation to be performed
    :param args[1]: The first number
    :param args[2]: The second number
    :args: The arguments passed to the program
    :args -a: The sum of the two numbers
    :args -s: The difference of the two numbers
    :args -m: The product of the two numbers
    :args -d: The quotient of the two numbers
    :args -po: The first number raised to the power of the second number
    :args -r: The remainder of the first number divided by the second number
    :args pr: The first number is prime
    """
    if len(args) > 0:
        if args[0] == "-a":
            print(functions.add(args[1], args[2]))
            return functions.add(args[1], args[2])
        elif args[0] == "-s":
            print(functions.subtract(args[1], args[2]))
            return functions.subtract(args[1], args[2])
        elif args[0] == "-m":
            print(functions.multiply(args[1], args[2]))
            return functions.multiply(args[1], args[2])
        elif args[0] == "-d":
            print(functions.divide(args[1], args[2]))
            return functions.divide(args[1], args[2])
        elif args[0] == "-po":
            print(functions.power(args[1], args[2]))
            return functions.power(args[1], args[2])
        elif args[0] == "-r":
            print(functions.divide(args[1], args[2]))
            return functions.divide(args[1], args[2])
        elif args[0] == "-pr":
            print(functions.is_prime(args[1]))
            return functions.is_prime(args[1])
        else:
            print("Invalid operation!")
            print("Enter 1 for addition")
            print("Enter 2 for subtraction")
            print("Enter 3 for multiplication")
            print("Enter 4 for division")
            print("Enter 5 for power")
            print("Enter 6 for remainder")
            print("Enter 7 to check if a number is prime")
            print("Enter 8 to exit")
            operation = input("Enter the operation you want to perform: ")
            if operation == "1":
                a = input("Enter the first number: ")
                b = input("Enter the second number: ")
                print(functions.add(a, b))
            elif operation == "2":
                a = input("Enter the first number: ")
                b = input("Enter the second number: ")
                print(functions.subtract(a, b))
            elif operation == "3":
                a = input("Enter the first number: ")
                b = input("Enter the second number: ")
                print(functions.multiply(a, b))
            elif operation == "4":
                a = input("Enter the first number: ")
                b = input("Enter the second number: ")
                print(functions.divide(a, b))
            elif operation == "5":
                a = input("Enter the first number: ")
                b = input("Enter the second number: ")
                print(functions.power(a, b))
            elif operation == "6":
                a = input("Enter the first number: ")
                b = input("Enter the second number: ")
                print(functions.divide(a, b))
            elif operation == "7":
                a = input("Enter the number: ")
                print(functions.is_prime(a))
            elif operation == "8":
                exit()
            else:
                print("Invalid operation!")
                exit()
    else:
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        print("Enter 5 for power")
        print("Enter 6 for remainder")
        print("Enter 7 to check if a number is prime")
        print("Enter 8 to exit")
        operation = input("Enter the operation you want to perform: ")
        if operation == "1":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            print(functions.add(a, b))
        elif operation == "2":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            print(functions.subtract(a, b))
        elif operation == "3":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            print(functions.multiply(a, b))
        elif operation == "4":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            print(functions.divide(a, b))
        elif operation == "5":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            print(functions.power(a, b))
        elif operation == "6":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            print(functions.divide(a, b))
        elif operation == "7":
            a = input("Enter the number: ")
            print(functions.is_prime(a))
        elif operation == "8":
            exit()
        else:
            print("Invalid operation!")
            exit()


if __name__ == "__main__":
    main()
