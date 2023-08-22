nivelAgua=int(input("Cual es el nivel de agua: ?"))
# evaluando multiples condiciones

if nivelAgua > 0 and  nivelAgua <= 200:
    print(f"el nivel de agua es: {nivelAgua}, esya muy bajo")
elif nivelAgua > 200 and nivelAgua <= 400:
    print(f"el nivel del agua es:{nivelAgua}, estasmos operabdo con normalidad")
elif nivelAgua > 400:
    print(f"el nivel del agua es: {nivelAgua}, inicie plan de evacuación...")
else:
    print("por favor revise el sensor del agua,  nivel de agua no valido")