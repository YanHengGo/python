def discounts(price,rate):
    final_price=price*rate
    old_price=50
    print('in function old_price : ',old_price)
    return final_price

old_price=float(input('please enter a price :'))
rate=float(input('please enter a rate :'))
new_price=discounts(old_price,rate)
print('global old_price:',old_price)
print('discounts :',new_price)
