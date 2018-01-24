friends_home = {
    'Michal' : 'Poznan',
    'Ola' : 'Krakow',
    'Bartek' : 'Berlin'
}

print(len(friends_home))
print(friends_home['Ola'])
friends_home['Ola'] = 'Zgorzelec'
print(friends_home['Ola'])

# czy klucz istnieje - ma znaczenie wielkość liter
print('Ola' in friends_home)
del(friends_home['Ola'])
print(friends_home.values())
print(friends_home.keys())


print('--------- zadanie 1 ----------')

friends_ex1 = {}

for num in range(2):
    userFriendName = input('Podaj imię Twojego znajomego: ')
    userFriendCity = input('Podaj miejsce zamieszkania: ')

    if userFriendCity in friends_ex1.values():
        print('nie potrzebuję więcej przyjaciół z ' + userFriendCity)
    else:
        friends_ex1[userFriendName] = userFriendCity

print(friends_ex1)

print('------------- FUNKCJE --------------------')

def funkcja_dubluj(argument):
    return argument * 2

print(funkcja_dubluj(4))

def obj_prostopadloscianu(x,y,z):
    return x*y*z

print((obj_prostopadloscianu(2,12,16)))

def koniec_programu():
    print('koniec programu. Naciśnij dowolny przycisk')
    input()

koniec_programu()

def foo(first, second, third):
    print('First: %s' %(first))
    print('Second: %s' %(second))
    print('Third: %s' %(third))

foo(1,2,3)

greetings = {
    'pl' : 'Witaj %s',
    'en' : 'Hello %s',
    'de': ' Hallo %s',
    'it': 'Ciao %s',
    'fr': 'Salut %s'
}

def where_are_you_from(name, country):
    if(country in greetings):
        print(greetings[country] %(name))
    else:
        print('Przykro mi nie umiem się przywitać w tym języku')

for num in range(3):
    userName = input('Podaj imię: ')
    userCountry = input('Podaj kraj: ')
    where_are_you_from(userName, userCountry)