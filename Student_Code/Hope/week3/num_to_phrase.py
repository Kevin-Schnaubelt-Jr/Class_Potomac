user_input= int(input("enter number >:"))


ones_table= {
    0:"zero",
    1:"one",
    2:"two" ,
    3:"three" ,
    4:"four" ,
    5:"five",
    6:"six" ,
    7:"seven" ,
    8:"eight" ,
    9:"nine" ,
}

outliers={
    10:"Ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteeen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    } 

tens_table={
    2:"twenty", 
    3:"thirty",
    4:"forty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety",
}






if user_input < 10:
    print(ones_table[user_input])
elif user_input in outliers: 
    print(outliers[user_input])
elif user_input >= 20:
    tens_place = user_input // 10
    ones_place = user_input % 10
    print(f"{tens_table[tens_place]}  {ones_table[ones_place]}")
   




    # first_number = user_input // 10
    # second_number = user_input % 10
    # print(di)