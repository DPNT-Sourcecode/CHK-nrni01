# noinspection PyUnusedLocal
# skus = unicode string
deals_order = ['E', 'A', 'B']
deals = {'A': {'quantity': 3, 'deal_price': 130},
         'B': {'quantity': 2, 'deal_price': 45},
         'E': {'quantity': 2, 'deal_price': 'B'}}

prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}


def checkout(skus):
    # skus = skus.upper()
    shopping_list = {}
    for item in skus:
        if item not in prices:
            return -1
        if item not in shopping_list:
            shopping_list[item] = 1
        else:
            shopping_list[item] += 1
    total = 0
    for item in deals_order:
        if item in shopping_list and deals[item]['quantity']<shopping_list[item]:
            if deals[item]

    for item in shopping_list:
        # if item in deals:
        #
        #     total += shopping_list[item] // deals[item]['quantity'] * deals[item]['deal_price'] + shopping_list[item] % \
        #              deals[item]['quantity'] * prices[item]
        # else:
        total += shopping_list[item] * prices[item]

    return total

