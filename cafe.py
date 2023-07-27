menu_list = ['tea', 'coffee', 'cake', 'sandwich']

stock_dict = {'tea': 50,
'coffee': 50,
'cake': 20,
'sandwich': 35
}

price_dict = {'tea': .5,
'coffee': .75,
'cake': 1.5,
'sandwich': 2.5
}

total_stock = 0
# Counter for cumaltive value of stock

for menu_item in price_dict:
# Iterate over all keys in the price dictionary

    value = stock_dict[menu_item] * price_dict[menu_item]
# Dictionaries in Python are data structures that store key-value pairs. When you provide a key, such as key, inside square brackets after the dictionary name (price_dict or stock_dict), Python looks up that key in the dictionary and returns the corresponding value associated with it.
# Value associated with the retrieved key in the stock dictionary multiplied by the value associated with the retrieved key in the price dictionary give the value of that specific menu item.

    total_stock += value
# Value of total stock (0) plus the total value of a specific menu item.

print(f"Total stock value: {total_stock}")