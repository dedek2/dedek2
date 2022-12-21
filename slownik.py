syn_ojciec = {}


def show_key_and_value():
    indeks_pary = 0
    for key, value in syn_ojciec.items():
        print(key, '-', value + '[' + str(indeks_pary) + ']')
        indeks_pary += 1


def add_key_and_value():
    imie_syna = input('Podaj imię i nazwisko syna: ')
    imie_ojca = input('Podaj imie i nazwisko ojca: ')
    syn_ojciec[imie_syna] = imie_ojca 
    print('Dodano nowe wartości do słownika')

def change_key_and_value():
    print('Podaj klucz  w słowniku który chcesz podmienić: ')
    imie_nazwisko_syna = input('Podaj imie i nazwisko syna: ')
    if imie_nazwisko_syna not in syn_ojciec:
        print('Nie ma takiego klucza w słowniku')
        return
    print('Podaj wartość klucza który podmieniłeś: ')
    imie_nazwisko_ojca = input('Podaj imie i nazwisko ojca: ')
    syn_ojciec[imie_nazwisko_syna] = imie_nazwisko_ojca
    print('Podmieniłeś zawartość słownika')

def delete_key_and_value():
    print('Która parę chcesz usunąć ze słownika')
    try:
        klucz = input('Podaj imię i nazwisko syna żeby usunąć parę ze słownika:')
        syn_ojciec.pop(klucz)
    except KeyError:
        print('Taki klucz nie istnieje')
        return
    print('Zawartość słownika została usunięta')

    
user_choice = -1
while user_choice !=5:

    print('------- Menu -------')
    print('1. Pokaż zawartość słownika')
    print('2. Dodaj imię i nazwisko syna i ojca')
    print('3. Podmień zawartość słownika.')
    print('4. Usuń zawrtość słownika.')
    print('5. Wyjdź')
    user_choice = int(input('Wybierz punkt z menu: '))


    if user_choice == 1:
        show_key_and_value()

    if user_choice == 2:
        add_key_and_value()

    if user_choice == 3:
        change_key_and_value()

    if user_choice == 4:
        delete_key_and_value()


    


