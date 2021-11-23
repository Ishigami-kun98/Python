number = float(input('insert a number'))
sconto = float(input('insert a discount value between 0 to 100 '))
if sconto < 0 or sconto > 100:
    print('value not good')
else :
    discount = (number * sconto)//100
    print('you inserted: ', number, ' and discount value is: ', sconto, ' discount value is: ', discount)
    finalValue = number - discount
    print('the final price is: ' , finalValue)
