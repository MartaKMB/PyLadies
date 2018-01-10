# typu mutowalne vs niemutowalne

marta = 'Marta'
idImienia = id(marta)
print(idImienia)

marta = 132
idImienia = id(marta)
print(idImienia)

slowa = ['Ala', 'ma', 'kota']
idTablicy = id(slowa)
print(idTablicy)

slowa.append('i')
slowa.append('psa')
idTablicy = id(slowa)
print(idTablicy)

zdanie = ''.join(slowa)
print(zdanie)

# true or false - przez cały okres działania programu są reprezentowane przez te same obiekty w pamięci
print(id(True))

prawda = True
print(id(prawda))

x = 5
prawda_cy_falsz = x < 10
print(id(prawda_cy_falsz))

# konwersja typów
tekst = '13'
tekst_na_int = int(tekst)

print(int(True))
print(float(False))

print(bool(0))
print(bool(0.2))
print(bool(-12))

print(bool(''))
print(bool(' '))

print(bool([]))
print(bool([1]))

imie = 'kkk'

print(f'Testowo witaj {imie}')

if imie is not None:
    print("Witaj {imie}")
else:
    print('Witaj nieznajomy! {imie}')

print(bool(None))

print(isinstance(imie, str))

lista1 = [1,2,3]
lista2 = [3,4,53]
lista_suma = lista1 + lista2

print(lista_suma)

x = 2
y = 'Ala'
print(x*y)

a = False
b = 'Ala'
print(a*b) #pusty łańcuch znaków

pusta_tablica = a*b
print(len(pusta_tablica))

# inne operatory: % - modulo // - podłoga z dzielenia, która jest float'em ** - potęgowanie, jest int lub float
print(16//3.3)
print(12.7//5)

print(2**4)
print(3**0.5) # pierwiastek

m = 4
m //= 2.5
print(m)

# operatory porównania - WARTOŚCI

f = 10
e = -2
r = 3
t = 123
if f > e and r < t:
    print('testujemy and')

s = 'apple'
w = 'banana'
print(s < w) # True, ale jak w = 'Banana', to będzie False
ww = "Banana"
print(s < ww)

print(chr(115))

lista_a = [1,2,3]
lista_b = [1,5,1]

if lista_b > lista_a:
    print('znalazłeś coś większego w lista_b i dalej nie sprawdzasz')

if lista_a is not lista_b:
    print('można używać is lub is not')

fg = 300
yt = 300
print(fg is yt) # True ???!!! - to jednak te same pokoje?
print(fg == yt)

# and i or

miasto = None
miejsce_zam = miasto or 'Poznań'
print(miejsce_zam)

'''
zmienna = '' or [] or ()
zmienna == () -> True
'''

# and zwracana jest ostatnia prawdziwa wartość

# ZADANIA
pusty_str = '' and True and [1,2,3]
print(len(pusty_str))

print('kot' and True or [1,2,3])
print('' or True and [])
print([1] or [] and ' ')
print(True and False and ())

print('***************************')

DOMYSLNY_PROMIEN_KM = 25

wiadomosc = ('Podaj zasieg')
podany_zasieg = abs(int(input(wiadomosc)))

zasieg = podany_zasieg or DOMYSLNY_PROMIEN_KM
print(f'Zasieg to {zasieg}')