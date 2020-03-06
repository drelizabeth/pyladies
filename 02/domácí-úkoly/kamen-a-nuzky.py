#Zkus přepsat Kámen, Nůžky, Papír pomocí and a or.Dokážeš docílit toho, aby se každý z
#  řetězců 'Plichta.', 'Počítač vyhrál.' a 'Vyhrála jsi!' objevil v programu jen jednou, 
# aniž bys tyhle řetězce musela přiřazovat do proměnných? Pokud ano, gratuluji!
tah_pocitace = 'kámen'
tah_cloveka = input('kámen, nůžky, nebo papír? ')

if (tah_cloveka == 'kámen' and tah_pocitace == 'nůžky') or (tah_cloveka == 'nůžky' and tah_pocitace == 'papír') or (tah_cloveka == 'papír' and tah_pocitace == 'kámen'): 
    print('Vyhrála jsi!') 
elif (tah_cloveka == 'kámen' and tah_pocitace == 'papír') or (tah_cloveka == 'nůžky' and tah_pocitace == 'kámen') or (tah_cloveka == 'papír' and tah_pocitace == 'nůžky'): 
    print('Počítač vyhrál.')
elif (tah_cloveka == 'kámen' and tah_pocitace == 'kámen') or (tah_cloveka == 'nůžky' and tah_pocitace == 'nůžky') or (tah_cloveka == 'papír' and tah_pocitace == 'papír'): 
    print('Plichta.') 
else:
    print('Nerozumím.')

