print("Bem-vindo ao Conversor de Temperatura!")
temp_celsius = float(input("Digite a temperatura em Celsius: "))

temp_fahrenheit = (temp_celsius * 9/5) + 32
temp_kelvin = temp_celsius + 273.15

print(f"A temperatura em Celsius é = {temp_celsius}°C")
print(f"A temperatura em Fahrenheit é = {temp_fahrenheit}°F")
print(f"A temperatura em Kelvin é = {temp_kelvin}K")