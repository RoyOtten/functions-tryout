
def tafel(input):
    for a in range (0,11):
        resultaat = a * input
        print(str(a) + " x " + str(input) + ' = ' + str(resultaat))

user = int(input("vul getal in loser: "))
tafel(user)
