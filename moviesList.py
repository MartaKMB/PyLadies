print('zajęcia 13.12')

filmy = ['Pocahontas', 'Król Lew', 'Bambi', 'Gdzie jest Nemo?', 'Spiderman', 'Batman', 'Pszczółka Maja', 'Smerfy']

#1
print('ZADANIE 1')
print(filmy[0])
print(filmy[6])
print(filmy[-1])
print(filmy[:4])

#wypisz 4 ostatnie
dlugosc_listy = len(filmy)
czwarty_od_konca = dlugosc_listy - 4
print(filmy[czwarty_od_konca:])

print(filmy[-4:])

#od 4 do 7
print(filmy[3:7])

#dodatkowe
film_5 = filmy[4]
litera_3 = film_5[2]
litery_2_do_6 = film_5[1:6]
print(litera_3)
print(litery_2_do_6)

#2
print('ZADANIE 2')
print('Renifer Niko ratuje Święta' in filmy)
filmy.append('Renifer Niko ratuje Święta')
print(filmy)

del filmy[4]
print(filmy[4])

nowy_film = input('Dodaj nowy tytuł do listy:\n')

nowy_film_1 = input('Dodaj kolejny tytuł do listy:\n')
nowy_film_2 = input('Dodaj drugi tytuł do listy:\n')
nowy_film_3 = input('Dodaj trzeci tytuł do listy:\n')

if nowy_film in filmy:
    print(nowy_film + ' jest już na liście')
elif nowy_film_1 in filmy:
    print(nowy_film_1 + ' jest już na liście')
elif nowy_film_2 in filmy:
    print(nowy_film_2 + ' jest już na liście')
elif nowy_film_3 in filmy:
    print(nowy_film_3 + ' jest już na liście')
else:
    filmy.extend([nowy_film, nowy_film_1, nowy_film_2, nowy_film_3])
    print(filmy)

print('ZADANIE DODATKOWE')

archiwum = []
