budzet = int(input('Podaj jaki masz budżet na prezenty świąteczne'))
print('Twój budżet to: ', budzet, ' Teraz odliczę podatek i kwotę na ZUS')

podatek = budzet * 0.19
print('Podatek od podanej kwoty wynosi: ', podatek)
print('ZUS to 1172.56zł')

ostateczna_kwota_na_pezenty = budzet - podatek - 1172.56
print('Ostateczna kwota na zakupy to:', ostateczna_kwota_na_pezenty)

suma_prezenty = 0
ile_prezentow = int(input('Podaj ile chcesz kupić prezentów: '))

for i in range(1,ile_prezentow+1):
    pytanie = 'Podaj cenę ', i, ' prezentu:'
    cena_prezentu = int(input(pytanie))
    suma_prezenty += cena_prezentu

print('Za wszystkie zakupy zapłacisz: ', suma_prezenty, 'zł')

if(suma_prezenty > ostateczna_kwota_na_pezenty):
    print('Niestety wydatki przekraczją Twój budżet')
else:
    print('Udanych zakupów!')