#Hozz létre egy változót ezzel az értékkel:
#“Hello World!”
#Írasd ki a változó értékét egyben!
#Írasd ki a változó értékét egyesével!
#Készíts egy függvényt ami kiírja a változó értékét!
#Készíts egy .py kiterjesztésű fájlt a mappádba és
#az előző feladatokat írd le oda is

helloString = "Hello World!"

print(helloString)

for i in helloString:
    print(i)


def helloWorldPrinter(wordToPrint):
    for i in wordToPrint:
        print(i)    

helloWorldPrinter(helloString)
        
