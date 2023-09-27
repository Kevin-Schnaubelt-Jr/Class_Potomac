units_to_meters={
    "feet":0.30483,
    "miles":1609.34
}

users_unit_of_mesurment=input("Feet or miles? : ")
user_distance=input("Give a distance. : ")
user_unit_convert=input(f"What do you want convert {users_unit_of_mesurment} to? : ")

print(float(user_distance) * units_to_meters[users_unit_of_mesurment] / units_to_meters[user_unit_convert])