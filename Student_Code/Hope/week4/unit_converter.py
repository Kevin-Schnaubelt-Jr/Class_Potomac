#1ft=0.3048)
#1mi=1609.34
#1m=1m
#1km=1000m

user_input= input("what unit are you converting?; feet, miles, meters, kilometers" )
if user_input == 'feet':


    feet=input("how many")
    ans= int(feet)*0.3048
    answer=round (ans,5)
    print(answer) 

elif user_input== "miles":
    miles=input("how many")
    ans=int(miles) *1609.34
    answer=round (ans,5)
    print(answer)

elif user_input == 'meter':
    meters=input("how many")
    print(user_input)

elif user_input == "kilometer":
    kilometer=input("how many")
    ans=int(kilometer)*1000
    answer=round (ans,5)
    print (answer)



