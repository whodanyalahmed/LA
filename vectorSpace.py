# Author @dan
# facebook : /whodanyalahmed
# twitter : /whodanyalahmed
# instagram : @whodanyalahmed
# linkedin : /in/whodanyalahmed


while True:
    print("\n\t\tVector Space")
    print("\t\t------------")
    print("1 - AC Additive Closure")
    print("2 - SC Scalar Closure")
    print("3 - C Commutativity")
    print("4 - AA Additive Associativity")
    print("5 - Z Zero Vector")
    print("6 - AI Additive Inverses")
    print("7 - SMA Scalar Multiplication Associativity")
    print("8 - DVA Distributivity across Vector Addition")
    print("9 - DSA Distributivity across Scalar Addition")
    print("10 - O One")
    print("E - Exit")

    op = input("Enter the option: ")

    if(op == "1"):
        val = eval(input("Enter number of values: "))
        ul = []
        vl = []
        result = []
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            v = eval(input("Enter v"+str(i)+": "))
            vl.append(v)
            ul.append(u)
            mul = vl[i] + ul[i]
            result.append(mul)
        print(ul)
        print(vl)
        print("The sum of u and v is : ", result)

    elif(op == "2"):

        val = eval(input("Enter number of values: "))
        ul = []
        result = []
        v = eval(input("Enter c: "))
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            ul.append(u)
            mul = ul[i]*v
            result.append(mul)
        print("u = ", ul)
        print("The sum of u and c is : ", (result))

    elif(op == "3"):
        val = eval(input("Enter number of values: "))
        ul = []
        vl = []
        result = []
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            v = eval(input("Enter v"+str(i)+": "))
            vl.append(v)
            ul.append(u)
            ad = vl[i] + ul[i]
            result.append(ad)
        print("u = ", ul)
        print("v = ", vl)
        print(str(ul) + " + " + str(vl) + " = ", result)
        print(str(vl) + " + " + str(ul) + " = ", result)

    elif(op == "4"):
        val = eval(input("Enter number of values: "))
        ul = []
        vl = []
        wl = []
        result = []
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            v = eval(input("Enter v"+str(i)+": "))
            w = eval(input("Enter w"+str(i)+": "))
            vl.append(v)
            ul.append(u)
            wl.append(w)
            ad = vl[i] + ul[i] + wl[i]
            result.append(ad)
        print("u = ", ul)
        print("v = ", vl)
        print("w = ", wl)
        print("( "+str(ul) + " + "+str(vl) + " ) + "+str(wl) + " = ", result)
        print(str(ul) + " + " + " ( " + str(vl) + " + " +
        str(wl) + " ) " + " = ", result)

    elif(op == "5"):
        val = eval(input("Enter number of values: "))
        ul = []
        result = []
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            ul.append(u)
            ad = ul[i]+0
            result.append(ad)
        print("u = ", ul)
        print("The sum of u and 0 is : ", (result))

    elif(op == "6"):
        val = eval(input("Enter number of values: "))
        ul = []
        result = []
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            ul.append(u)
            mul = ul[i]-ul[i]
            result.append(mul)
        print("u = ", ul)
        print("The sum of u and 0 is : ", (result))

    elif(op == "7"):
        val = eval(input("Enter number of values: "))
        ul = []
        result = []
        a = eval(input("Enter α: "))
        b = eval(input("Enter β: "))
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            ul.append(u)
            mul = ul[i]*a*b
            result.append(mul)
        print("u = ", ul)
        print("a = ", a)
        print("b = ", b)
        print("( "+str(a)+" * "+str(b) + " ) "+str(ul) + " = ", result)
        print(str(a)+"( "+str(b)+" * " + str(ul) + " ) " + " = ", result)
    elif(op == "8"):
        val = eval(input("Enter number of values: "))
        ul = []
        vl = []
        result = []
        a = eval(input("Enter α: "))
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            v = eval(input("Enter v"+str(i)+": "))
            ul.append(u)
            vl.append(v)
            mul = a*(ul[i] + vl[i])
            result.append(mul)

        print("u = ", ul)
        print("v = ", vl)
        print("a = ", a)
        print("( "+str(ul)+" * "+str(vl) + " ) "+str(a) + " = ", result)
        print(str(a)+" * "+str(ul) + " + "+str(a)+" * "+str(vl) + " = ", result)

    elif(op == "9"):
        val = eval(input("Enter number of values: "))
        ul = []
        result = []
        a = eval(input("Enter α: "))
        b = eval(input("Enter β: "))
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            ul.append(u)
            mul = ul[i]*(a + b)
            result.append(mul)
        print("u = ", ul)
        print("a = ", a)
        print("b = ", b)
        print("( "+str(a)+" * "+str(b) + " ) "+str(ul) + " = ", result)
        print(str(a)+" * "+str(ul) + " + "+str(b)+" * "+str(ul) + " = ", result)

    elif (op == "10"):
        val = eval(input("Enter number of values: "))
        ul = []
        result = []
        for i in range(val):
            u = eval(input("Enter u"+str(i)+": "))
            ul.append(u)
            ad = ul[i]*1
            result.append(ad)
        print("u = ", ul)
        print("The product of 1 with u is : ", (result))

    elif (op == "e" or op == "E"):
        break
    else:
        print("Enter valid option/Try again")
