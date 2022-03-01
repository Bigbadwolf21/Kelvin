3# Ask the user for kelvin's input
kelvin = input("Enter the value of Kelvin here ")
kelvin = int(kelvin)
#Get the value of celsius by deducting 273 from kelvin
celsius = kelvin - 273
# Determine the value of fahrenheit
fahrenheit = celsius * (9/5) + 32
# Convert fahrenheit to integer value
fahrenheit = int(fahrenheit)
# Determine the newton
newton = celsius * (33/100)
# convert newton to integer
newton = int(newton)
# Print al the values
# print temperature in fahrenheit
print(f"The temperature is {fahrenheit} degrees Fahrenheit.")
# convert kelvin to fahrenheit
print(f"{kelvin} Kelvin is about {fahrenheit} degrees Fahrenheit")
# print temperature in celsius
print(f"The temperature is {celsius} degrees Celsius")
# Convert kelvin to celsius
print(f"{kelvin} Kelvin is about {celsius} degrees Celsius")
# print temperature in newton
print(f"The temperature is {newton} degrees Newton")
# convert kelvin to newton
print(f"{kelvin} Kelvin is about {newton} degrees Newton")
