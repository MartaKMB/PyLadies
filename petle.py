print('for')

liczby = [2,3,5,7]
for liczba in liczby:
    print(liczba)

print('while')

licznik = 0
while licznik < 5:
    print(licznik)
    licznik += 1

#pętla for dla kolejnych znaków w stringu
for letter in 'Python':
    print('Bieżąca litera: ', letter)

#dla elementów list
fruits = ['banan', 'jabłko', 'gruszka']
for fruit in fruits:
    print('Owoc: ', fruit)

#dla zakresu liczb
for num in range(10,20):
    print(num)

'''  
range nie uwzgględnia liczby w nawiasie
range(kiedy_stop)
range(start, kiedy_stop)
range(start, kiedy_ctop, krok)
kiedy_stop - do niej ale bez niej
'''

print('*************************')
#zad 1
for num in range(0,27,2):
    print(num)

i = 0
for i in range(27):
    if(i%2 == 0):
        print(i)

#zad 2
osoby = ['Monika', 'Robert', 'Krzyś']
for osoba in osoby:
    print('Wesołych Świąt!', osoba)

#zad 3
zdanie = 'Ala ma 4 koty'
counter = 0
for znak in zdanie:
    counter +=1
    if znak.isdigit():
        print(znak, 'jest liczbą i jest na pozycji', counter)

#zadanie pętla for i while - średnie wynagrodzenie

print('średnie wynagrodzenie w 2017 roku')

suma_zarobkow = 0
for i in range(0,12):
    wynagrodzenie = int(input('podaj wynagrodzenie w pętli for:'))
    suma_zarobkow = suma_zarobkow + wynagrodzenie

print(suma_zarobkow/12)

'''
suma = 0
miesiac = 1
while(miesiac<13):
    wynagrodzenie_while = int(input('Podaj wynagrodzenie w pętli while'))
    suma += wynagrodzenie_while
    miesiac += 1

print(suma/12)
'''

#przerwanie pętli break
print('break i continue')

while True:
    numer_do_break = int(input('Podaj liczbę'))
    print(numer_do_break)
    if numer_do_break == 0:
        break

#continue

for num in range(2,10):
    if num % 2 == 0:
        print('Liczba parzysta', num)
        continue
    print('Liczba nieparzsta', num)
