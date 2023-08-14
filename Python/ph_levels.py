
ph = int(input("Pick a number(0-14): "))

if ph > 7:
    print(ph, "is Basic")
elif ph < 7:
    print(ph, "is Acidic")
else:
    print(ph, "is Neutral")