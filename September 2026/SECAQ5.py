#covert temperature from Celsius to Fahrenheit

cel = float(input("Enter the temperature in celsius degree:"))

fah = (9/5*cel) + 32   # fah means temperature in Fahrenheit
if cel<=1:
    a = "degree"
else:
    a = "degrees"
print("The temperature in Celsius is",cel,a,".")
if fah<=1:
    b = "degree"
else:
    b = "degrees"
print("The temperature in Fahrenheit is",fah,b,".")