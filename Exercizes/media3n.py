m1 = int(input('inserisci il primo valore da 18 a 30 '))
m2 = int(input('inserisci il secondo valore da 18 a 30 '))
m3 = int(input('inserisci il terzo valore da 18 a 30 '))
if (m1 and m2 and m3) > 17 and (m1 and m2 and m3) < 31 :
    media =(m1 + m2 + m3)/3
    if(media > 28):
        print('good work' , media)
    else:
        print('media is ', media)

else :
    print('trashcan')
