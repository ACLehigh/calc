while True:

    print("------------")

    print("Calculators")

    print("------------")

    print("1. Math Calculator")

    print("2. Percentage Calculator")

    print("3. Square/Cube Calculator")

    print("4. Age Calculator")

    print("5. Temperature Calculator")

    print("6. Weight Calculator")

    print("7. Circle Area Calculator")

    print("8. Triangle Area Calculator ")

    print("9. Finish")

    a=int(input("Choose an option. "))

    if a==1:

        num=int(input("Enter a number. "))

        sym=input("Enter a math symbol. ")

        num2=int(input("Enter a second number. "))

        if sym=="+":

            print(f"Your answer is {num+num2}.")

        elif sym=="-":

            print(f"Your answer is {num-num2}.")

        elif sym=="*":

            print(f"Your answer is {num*num2}.")

        elif sym=="/":

            print(f"Your answer is {num/num2}.")

    elif a==2:

        print("------------")

        print("1. Value of Percent")

        print("2. Percent of Value")

        per=int(input("Choose an option. "))

        if per==1:

            print("------------")

            one=float(input("Enter the base number. "))

            one2=float(input("Enter the percent of the base. "))

            print(f"The number that is {one2}% of {one} is {(one*one2)/100}")

        if per==2:

            print("------------")

            two=float(input("Enter the base number. "))

            two1=float(input("Enter the percent value. "))

            print(f"The number {two1} is {(two1*100)/two}% of {two}")

    elif a==3:

        print("------------")

        print("1. Square of Number")

        print("2. Cube of Number")

        exp=int(input("Choose an option. "))

        if exp==1:

            print("------------")

            three=int(input("Enter the number you want squared. "))

            print(f"{three} squared is {three*three}")

        elif exp==2:

            print("------------")

            three=int(input("Enter the number you want cubed. "))

            print(f"{three} cubed is {(three*three)*three}")

    elif a==4:

        age=int(input("Enter your date of birth. "))

        print(f"You are {2025-age} years old.")

    elif a==5:

        print("------------")

        print("1. Fahrenheit to Celsius")

        print("2. Celsius to Fahrenheit")

        temp=int(input("Choose an option. "))

        if temp==1:

            fahr=int(input("Enter a fahrenheit temperature. "))

            print(f"Your temprature in celsius is {(fahr-32)/1.8}°.")

        if temp==2:

            cel=int(input("Enter a celsius temperature. "))

            print(f"Your temperature in fahrenheit is {cel*1.8+32}°.")

    elif a==6:

        print("------------")

        print("1. Pounds to Kilograms")

        print("2. Kilograms to Pounds")

        weight=int(input("Choose an option. "))

        if weight==1:

            print("------------")

            pound=int(input("Enter a pound weight. "))

            print(f"Your weight in kilograms is {(pound)/2.205}")

        elif weight==2:

            print("------------")

            kilo=int(input("Enter a kilogram weight. "))

            print(f"Your weight in pounds is {(kilo)*2.205}")

    elif a==7:

        area=int(input("Enter a radius. "))

        print(f"The area of your circle is {3.14*area*area} units^2.")

    elif a==8:

        base=int(input("Enter your triangle's base length. "))

        height=int(input("Enter your triangle's height. "))

        print(f"The area of your circle is {(base*height)/2}")

    elif a==9:

        print("------------")

        break