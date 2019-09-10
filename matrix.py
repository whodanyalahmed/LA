# Author @dan
# facebook : /whodanyalahmed
# twitter : /whodanyalahmed
# instagram : @whodanyalahmed
# linkedin : /in/whodanyalahmed

import pandas as pd
import numpy as np
while True:

    print("\n\t\tMatrix")
    print("\t\t------------")
    print("1 - Multiplication of Matrix")
    print("2 - Transpose of Matrix")
    print("E - Exit")

    op = input("Enter the option: ")

    if (op == "1"):

        x = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

        y = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

        z = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
        for i in range(len(x)):
            for r in range(len(x[0])):
                ival = eval(input("Enter value for x" + str(i+1) + str(r+1) + " : "))
                x[i][r] = ival
        print("===============================")

        for i in range(len(y)):
            for r in range(len(y[0])):
                ival = eval(input("Enter value for y" + str(i+1) + str(r+1) + " : "))
                y[i][r] = ival

        # iterate number of lines in matrice
        for i in range(len(x)):
            # iterate number of
            for r in range(len(y[0])):
                for k in range(len(y)):
                    z[i][r] += x[i][k] * y[k][r]
        print("x = ", x)
        print("y = ", y)
        
        print("x * y = ", )
        for i in z:
            print(i)

    elif(op == "2"):

        x = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

        result = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

        # iterate through rows
        for i in range(len(x)):
        # iterate through columns
            for j in range(len(x[0])):
                for k in range():
                    result[j][i][k] = x[k][i][j]


        

        for r in result:
            print(r)

    elif (op == "e" or op == "E"):
        break
    else:
        print("Enter valid option/Try again")