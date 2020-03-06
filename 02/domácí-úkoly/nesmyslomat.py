#Na srazu jsme měli program, který píše různé nesmysly podle uživatelem zadaného věku.
# Zkus napsat program, který píše hlášky podle zadané rychlosti chůze, váhy ulovené ryby, počtu tykadel,
# teploty vody nebo třeba vzdálenosti od rovníku. Podle toho, jak jste se na sraze domluvili, 
# pošli řešení e-mailem (např. organizátorům, koučovi, nebo vůbec). Posílej ho jako přílohu,
# nekopíruj ho do textu e-mailu. Jestli procházíš kurz sama a můžeš programování konzultovat 
# s někým zkušenějším, je tento úkol na takovou konzultaci ideální téma.
print('Odpovídej jen číslem.')
vaha = int(input('Kolik kilo má tvá ulovená ryba?'))
if vaha >= 20000:
    print('Gratulujeme k ulovení plejtváka!')
elif vaha >= 60:
    # Tahle větev se např. pro "20000" už neprovede.
    print('Delfíni by se němli lovit. Vrať ho do vody.')
elif vaha >= 5:
    print('Skvělé, na štice si pochutnáš.')
elif vaha >= 0:
    print('Chytit tak malou rybu, dá zabrat. Super, i sadrinka je skvělý úlovek. ')
else:
    # Nenastala ani nedna ze situací výše – muselo to být záporné
    print('Příště zkus radši chytat ryby než chytat lelky.')