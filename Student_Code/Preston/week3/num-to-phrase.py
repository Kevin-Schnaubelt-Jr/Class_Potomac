dict = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen"
}
dict2 = {
    2:"twenty ",
    3:"thirty ",
    4:"fourty ",
    5:"fifty ",
    6:"sixty ",
    7:"seventy ",
    8:"eighty ",
    9:"ninety "
}
dict3 = {
    0:"",
    1:"one hundred",
    2:"two hundred",
    3:"three hundred",
    4:"four hundred",
    5:"five hundred",
    6:"six hundred",
    7:"seven hundred",
    8:"eight hundred",
    9:"nine hundred"
}
def convert(user,dict,dict2,dict3):
    if user<20:
        return (dict[user])
    elif user>19 and user<100 and not user-((user//10)*10)==0:
        converted = (dict2[user//10]+dict[user-((user//10)*10)])
    elif user>100 and not user-((user//10)*10)==0:
        converted = (dict3[user//100]+dict2[user-(((user//100)*100))]+dict[user-((user//100)*100)])
    elif user>19 and user<100 and user-((user//10)*10)==0:
        converted = (dict2[user//10])
    return converted
#fix line 51 later
user = int(input("type a number"))
print(convert(user,dict,dict2,dict3))