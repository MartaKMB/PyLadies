x = 15
spr = x > 10 and "test"
print(spr)
print([] and x < 10)

print('kocur' or False and 'kot')

for element in range(1,5):
    print(element)

# # zadanie 1
print('zadanie 1')

listaSamoglosek = ['A', 'E', 'Y', 'I', 'O', 'U']
zdanieUzytkownika = input('napisz wyraz, a ja wypiszę wszystkie samogłoski: ')

for litera in zdanieUzytkownika:
    if(litera.upper() in listaSamoglosek):
        print(litera.upper())

# zadanie 2
print('zadanie 2')

wysokoscChoinki = int(input('jak wysoką chcesz choinkę?'))
gwiazdki = '*'
spacje = ' '
liczba_spacji_na_poczatku = wysokoscChoinki - 1
liczba_gwiazdek = 1;

for rzad in range(wysokoscChoinki):
    print((spacje * liczba_spacji_na_poczatku) + (gwiazdki * liczba_gwiazdek))
    liczba_spacji_na_poczatku -= 1
    liczba_gwiazdek += 2
