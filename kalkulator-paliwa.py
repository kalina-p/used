print('kalkulator zużycia paliwa')

koszt_paliwa = float(input('wpisz koszt 1 litra paliwa '))

kilometry = float(input('wpisz ilość kilometrów '))

srednie = float(input('wpisz średnie spalanie na 100km '))

ilosc = kilometry / 100

wynik = koszt_paliwa * srednie * ilosc

print('##########################################')
print("zapłacisz {:.2f} zł za {} km".format(wynik, kilometry))
print('##########################################')
