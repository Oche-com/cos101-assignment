print("COS101 Assignment")
print("Name of Functions")
print("Compound Interest")
#def compound_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
n = float(input("Enter the number of times interest is compounded per year: "))
amount = principal * (1 + rate/(100*n))**(n*time)
compound_interest = amount - principal
print("The compound interest is:", compound_interest)

print("Conversion of Celsius to Fahrenheit")
#def calculate_Celsius_to_fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

print("Simple Interest")
#def calculate_simple_interest
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)

print("Area of a Circle")
#def the_area_of_a_circle2
radius = float(input("Enter the radius of the circle: "))
area = 3.142* radius * 2
print("The area of the circle is:", area)

print("Conversion of Fahrenheit to Celsius")
#def calculate_Fahrenheit_to_Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)
