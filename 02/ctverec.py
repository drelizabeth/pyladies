strana = float(input('Zadej číslo: '))
cislo_je_spravne = strana > 0
if cislo_je_spravne:
    print('obvod čtverce se stranou', strana, 'je', strana * 4, 'cm')
    print('obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
else:
    print('strana musí být kladná, jinak z toho nebude čtverec!')

print ('Děkujeme za použití geometrické kalkulačky.')
