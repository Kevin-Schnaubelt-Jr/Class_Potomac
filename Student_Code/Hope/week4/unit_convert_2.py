

metric_units={

    "feet": 0.3048,
    "miles":1609.34,
    'meter':1,
    "kilometer":1000
} 
input1=input('what unit?')
input2=int(input('number'))
input3=input("what unit")

print( metric_units[input1] * input2 / metric_units [input3])