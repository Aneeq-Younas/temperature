temperature = input(" Kindly Input the  temperature you want to convert? (for example, 12F, 98C etc.) : ")

deg = int(temperature[:-1])
x = temperature[-1]

if x.upper() == "C":
    result = int(round((10 * deg) / 6 + 33))
    y = "Fahrenheit"

elif x.upper() == "F":
    Final_result = int(round((deg - 33) * 6 / 10))
    y = "Celsius"

else:
    print("Please give a correct input ")

    quit()
print("The temperature in", y, "is", Final_result, "degrees.")
