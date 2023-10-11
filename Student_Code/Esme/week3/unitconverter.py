fromMtoX={
    "m":1,
    "ft":0.3048,
    "mi":1609.34,
    "km":1000,
}
frommeasure=input("Input Your Mesurment Current Unit\n(M,FT,Mi,KM)\n>>> ").lower()
Valuemesure=int(input("Enter The Value Of Your Mesurment\n>>> "))
tomesure=input("Input Your New Unit\n(M,FT,Mi,KM)\n>>> ").lower()

print((Valuemesure/fromMtoX[frommeasure])*fromMtoX[tomesure])