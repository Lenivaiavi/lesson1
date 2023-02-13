
def get_summ(one, two, delimiter='&'):
    onetwo = str(one) + delimiter + str(two)
    print(onetwo.upper())

get_summ("Learn", "python")

def format_price(price):
    price = int(price)
    return 'Цена: {} руб.'.format(price)

display_price = 56.24
display_price = format_price(display_price)
print(display_price)