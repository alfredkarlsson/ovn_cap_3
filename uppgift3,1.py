import time

print("Välkommen till kundservice.")
print("Vi erbjuder tre olika abonnemang. 'Kontant', 'Normal' och 'Plus'")
print("")
input("Skriv något här och tryck på enter för att fortsätta.")

print("")
print("")


print("Vi hjälper dig avgöra vilket av de tillgängliga abonnemangen som är bäst för just ditt behov.")
print("")
input("Skriv något här och tryck på enter för att fortsätta.")


print("")
print("")

print("Svaret du ger bör endast anges i siffor. Du skall alltså lämna ute bokstäver och specialtecken.")
print("Dina svar skall även vara angivna i form av heltal.")
print("")

print("")
print("")


svar = input("Hur många minuter ringer du varje månad?")


svar = int(svar)

if svar <= 33:
    print("Kontant är det bästa abonnemanget för dig!")

if svar > 33 and svar < 67:
    print("Normal är det bästa abonnemanget för dig!")

if svar > 66:
    print("Plus är det bästa abonnemanget för dig!")

time.sleep(2)
