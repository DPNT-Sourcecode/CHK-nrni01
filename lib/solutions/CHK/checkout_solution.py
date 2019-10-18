# noinspection PyUnusedLocal
# skus = unicode string
deals_order = ['E', 'A', 'B']
deals = {'A': {'quantity': 3, 'deal': 130},
         'B': {'quantity': 2, 'deal': 45},
         'E': {'quantity': 2, 'deal': 'B'}}

prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}


def checkout(skus):
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

        if item in shopping_list and deals[item]['quantity'] <= shopping_list[item]:

            if isinstance(deals[item]['deal'], int):

                total += shopping_list[item] // deals[item]['quantity'] * deals[item]["deal"]
                shopping_list[item] = shopping_list[item] % deals[item]['quantity']

            else:

                if deals[item]['deal'] in shopping_list:

                    shopping_list[deals[item]['deal']] -= shopping_list[item] // deals[item]['quantity']

                    if shopping_list[deals[item]['deal']] < 0:
                        shopping_list[deals[item]['deal']] = 0

    for item in shopping_list:

        total += shopping_list[item] * prices[item]

    return total




