#1ft = 0.3048m
#1mi = 1609.34
#1m = 1m
# 1km = 1000m

# Define the unit conversion factors in a dictionary
unit_factors = {
    "kilometers": {
        "miles": 0.621371,
        "feet": 3280.84,
        "meters": 1000,
    },
    "miles": {
        "kilometers": 1.60934,
        "feet": 5280,
        "meters": 1609.34,
    },
    "feet": {
        "kilometers": 0.0003048,
        "miles": 0.000189394,
        "meters": 0.3048,
    },
    "meters": {
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
    },
}

def convert_units(value, from_unit, to_unit):
    if from_unit in unit_factors and to_unit in unit_factors[from_unit]:
        factor = unit_factors[from_unit][to_unit]
        result = value * factor
        return result
    else:
        return "Invalid conversion units."

# Get user input for conversion
while True:
    try:
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the input unit (kilometers, miles, feet, meters): ").lower()
        to_unit = input("Enter the output unit (kilometers, miles, feet, meters): ").lower()

        result = convert_units(value, from_unit, to_unit)
        if type(result) == str:
            print(result)
        else:
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        
        another_conversion = input("Do you want to convert another value? (yes/no): ").lower()
        if another_conversion != "yes":
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
