#zajęcia 13.12
#1

lista_liczb = [1, 2, 40+5]
lista_liczb_2 = [3, 56, -8]
lista_liczb_3 = ['tak', 'nie']

lista_liczb_razem = [lista_liczb, lista_liczb_2, lista_liczb_3]
print(lista_liczb_razem)

#przykład z czytelnictwem

lista_stron = [20, 0, 13, 0, 0, 45, 3, 3, 10]
print(lista_stron[4])

#ostatni element na liście -1
print(lista_stron[-1])

#długość listy len(nazwa tablicy)

dlugosc_listy = len(lista_stron)
ostatni_element = len(lista_stron) - 1
print(dlugosc_listy)
print(lista_stron[ostatni_element])

'''
komentarz
wielo
liniowy
'''

# pozycje od do

print(lista_stron[3:]) #od czwartej do ostatniej
lista_stron[2:4] #od trzeciej do czwartej
lista_stron[:3] #od pierwszej do trzeciej

#2

#czy element jest w liscie

moi_znajomi = [
    'Kunegunda',
    'Tomasz',
    'Jeremi',
    'Anastazja'
]

#element którego szukamy in
print('Ania Kowalska' in moi_znajomi) #False
print('Kunegunda' in moi_znajomi) #True

#dodanie elementu append
moi_znajomi.append('Grzegorz')
print(moi_znajomi)

#usuwanie del
#znamy pozycję del lista[pozycja]
del moi_znajomi[1]

#nie znamy pozycji: remove
moi_znajomi.remove('Anastazja')

print(moi_znajomi)

'''
#z inputem
nowy_znajomy = input('Jak masz na imię?\n') #kursor w nowej linii \n
moi_znajomi.append(nowy_znajomy)

nowy_znajomy_1 = input('Podaj imię:')
nowy_znajomy_2 = input('Podaj imię:')
nowy_znajomy_3 = input('Podaj imię:')
nowy_znajomy_4 = input('Podaj imię:')
nowy_znajomy_5 = input('Podaj imię:')

#doda listę elementów, jako listę w liście
# moi_znajomi.append([nowy_znajomy_1, nowy_znajomy_2, nowy_znajomy_3, nowy_znajomy_4, nowy_znajomy_5])

#połączenie list w jedną extend()
moi_znajomi.extend([nowy_znajomy_1, nowy_znajomy_2, nowy_znajomy_3, nowy_znajomy_4, nowy_znajomy_5])
print(moi_znajomi)
'''

#zajęcia 20.12
print('pętle, zajęcia 20.12')

#zapytaj o imię i nazwisko
for znajomy in range(5):
    do_inputu = 'Podaj imię:', len(moi_znajomi)+1, 'znajomego'
    nowe_imie = input(do_inputu)
    moi_znajomi.append(nowe_imie)

print(moi_znajomi)

licznik = 0
while licznik < 5:
    nowe_imie_while = input('Podaj imię po pętli while: ')
    moi_znajomi.append(nowe_imie_while)
    licznik += 1

print(moi_znajomi)