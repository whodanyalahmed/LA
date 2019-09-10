
# Author @dan
# facebook : /whodanyalahmed
# twitter : /whodanyalahmed
# instagram : @whodanyalahmed
# linkedin : /in/whodanyalahmed

import math

while True:
    print("\n\t\tVector")
    print("\t\t------\n")
    print("1 - Dot (.) Product")
    print("2 - Length")
    print("3 - Unit Vector")
    print("4 - Vector Addition")
    print("5 - Scalar Multiple")
    print("E - Exit")

    op = input("Enter the option: ")
    if(op == "1"):
        try:
            val = eval(input("Enter number of values: "))
            ul = []
            vl = []
            result = []
            for i in range(val):
                u = eval(input("Enter u"+str(i+1)+": "))
                ul.append(u)

            for i in range(val):
                v = eval(input("Enter v"+str(i+1)+": "))
                vl.append(v)
                mul = ul[i] * vl[i]
                result.append(mul)

            final = []
            c = 0
            for r in result:
                c = c + r
            final.append(c)
            print("u = ", ul)
            print("v = ", vl)
            print("( "+str(ul)+" * "+str(vl) + " )  = ", result)
            print("( "+str(ul)+" * "+str(vl) + " )  = ", final)

        except SyntaxError as e:
            print("You had SyntaxError")

    elif (op == "2"):
        try:
            val = eval(input("Enter number of values: "))
            ul = []
            result = []
            for i in range(val):
                u = eval(input("Enter u"+str(i+1)+": "))
                ul.append(u)
                mul = ul[i] * ul[i]
                result.append(mul)
            print("The of u is: ", ul)
            print("The square of u is : ", result)

            ans = 0
            for i in result:
                ans = ans + i
            print("The final under root ans is: ", ans)
            print("||u|| : ", math.sqrt(ans))

        except SyntaxError as e:
            print("You had SyntaxError")

    elif(op == "3"):
        try:
            val = eval(input("Enter number of values: "))
            ul = []
            result = []
            for i in range(val):
                u = eval(input("Enter u"+str(i+1)+": "))
                ul.append(u)
                mul = ul[i] * ul[i]
                result.append(mul)
            print("The of u is: ", ul)
            print("The square of u is : ", result)

            ans = 0
            for i in result:
                ans = ans + i
            print("||u|| : \u221A or", ans)
            print("||u|| : ", math.sqrt(ans))
            for i in ul:
                print(" ( "+str(i) + " / " + "\u221A" + str(ans) + " )", end="")

        except SyntaxError as e:
            print("You had SyntaxError")
    elif(op == "4"):
        try:
            val = eval(input("Enter number of values: "))
            ul = []
            vl = []
            result = []
            for i in range(val):
                u = eval(input("Enter u"+str(i+1)+": "))
                ul.append(u)
            for i in range(val):
                v = eval(input("Enter v"+str(i+1)+": "))
                vl.append(v)
                sum = ul[i]+vl[i]
                result.append(sum)

            print("The sum of u : " + str(ul) + " and v : " + str(vl) + " is : " + str(result))
        except SyntaxError as e:
            print("You had SyntaxError")

    elif(op == "e" or op == "E"):
        break
    else:
        print("Enter valid option/Try again")
