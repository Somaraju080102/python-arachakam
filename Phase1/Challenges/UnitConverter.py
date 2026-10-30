
print("Welcome to Unit Converter CLI")

value=input("Enter the value to convert: ")

print("Choose the conversion type from the following options:")

print("1. km to miles")
print("2. Celsius to Farenhit")
print("3. Kg to Pounds")

conversionType=input("Enter the conversion type : ")

# Km to Miles formula is divide by 1.60934

if(conversionType == "1"):
    result = float(value) / 1.60934
    print(f"{value} km is equal to {result:.2f} miles")
elif(conversionType == "2"):
    result = (float(value) * 9/5) + 32
    print(f"{value} Celsius is equal to {result:.2f} Farenhit")
elif(conversionType == "3"):
    result = float(value) * 2.20462
    print(f"{value} Kg is equal to {result:.2f} Pounds")
else:
    print("Invalid conversion type")



