def cedric():
    var1 = "cedric"
    return var1


def yesOrno(vraag): 
    while True:
        antwoord = input(vraag) 
        if antwoord == "ja":
            return True
        elif antwoord == "nee":
            return False
        else:
            print("invalid Option") 



print("welcome to the game") 
print("this is a game that is basically ai tinder") 
print("you can pick a character and you can talk to them") 
print("lets begin") 

wie = input("wie van de mensen wil je kiezen \n")
if wie == cedric():
    print ("hoi, ik ben cedric ik hou me vooral bezig met coding en games") 
    vraagdate = input("kies wat je wilt zeggen tegen cedric.. let op , zijn intresses zijn belangrijl ,kies uit bowlen lasergamen en een film kijken\n")
    if vraagdate ==("bowlen"):
        print("cedric voelt zich beledigd door wat voor een saai idee dit is en heeft zijn intresse verloren") 
    elif vraagdate ==("een film kijken"):
        print("cedric voelt zich beledigd over jouw keuze en heeft zijn intresse in je verloren")
    elif vraagdate ==("lasergamen"):
        print("cedric kijkt blij en is meer geintresseerd in je") 
        print ("jullie gaan naar de bowlingbaane en hebben een leuke avond") 
        if yesOrno("cedric vond het een leuke avond en vraagt of je nog een avond met hem wilt afspreken, zeg je ja of nee?"): 
            print ("cedric kijkt je blij aan en begint te praten over wat hij verder wilt doen")
        else: 
            print ("cedric rent in verdriet naar zijn dungeons and dragons groep")
        
    

           
        



