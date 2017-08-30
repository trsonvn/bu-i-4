prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}

purchased_items= [
    {"banana" : 5}, {"orange" : 3}
]
total = 0
for item in purchased_items :
    for key in item :
        print ( "{0}, quantity: {1}, unit price: {2}".format( key, item[key], prices[key] ) )
        pay = item[key] * prices[key]
        print(" the amount you pay {0} is {1}$".format(key,pay))
        total += pay

print ("Total amount you need to pay: {0}$".format( total))