# -*- coding: utf-8 -*-
"""Stack Visualizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18vNqT8d2U1JLZpwNs9K3A0uE_U1vtDUs
"""

stack = []

while True:
    userInput = input('Enter the next instruction:')
    if(userInput == 'quit'):
        break
    elif(userInput == "pop"):
        stack.pop()
    else:
        number = int(userInput[5:])
        stack.append(number)
    print('The stack is: bottom', end=' ')
    for item in stack:
        print(item, end=' ')
    print('top')