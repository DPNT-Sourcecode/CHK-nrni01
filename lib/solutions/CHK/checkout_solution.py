# noinspection PyUnusedLocal
# skus = unicode string
deals_order = ['E','N', 'R','U','A', 'B', 'F','H','K','P','Q','V']

current_deals = {'A': [{'quantity': 5, 'deal': 200}, {'quantity': 3, 'deal': 130}],
                 'B': [{'quantity': 2, 'deal': 45}],
                 'E': [{'quantity': 2, 'deal': 'B'}],
                 'F': [{'quantity': 3, 'deal': 20}],
                 'H': [{'quantity': 10, 'deal': 80},{'quantity': 5, 'deal': 45}],
                 'K': [{'quantity': 2, 'deal': 150}],
                 'N': [{'quantity': 3, 'deal': 'M'}],
                 'P': [{'quantity': 5, 'deal': 200}],
                 'Q': [{'quantity': 3, 'deal': 80}],
                 'R': [{'quantity': 3, 'deal': 'Q'}],
                 'U': [{'quantity': 3, 'deal': 80}],
                 'V': [{'quantity': 3, 'deal': 130},{'quantity': 2, 'deal': 90}]}

prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G':20,'H':,'I':35,'J':60,'K':,'L':90,'M':15,'N':,'O':10,'P':,'Q':,'R':,'S':30,'T':20,'U':,'V':,'W':20,'X':90,'Y':10,'Z':50}


def checkout(skus):
    # a dictionary containing as key item name and as value number of items in the skus
    shopping_list = {}

    # turn the skus styring into shopping_list dictionary
    for item in skus:

        if item not in prices:
            return -1

        if item not in shopping_list:
            shopping_list[item] = 1

        else:
            shopping_list[item] += 1

    # total for checkout
    total = 0

    # check if the items with deals are on the shopping list
    for item in deals_order:

        # get each deal for an item
        for deals in current_deals[item]:

            # check if quantity required for the deal is in the shopping list
            if item in shopping_list and deals['quantity'] <= shopping_list[item]:

                # if the deal is a price deal => add that to total and update the shoping list
                if isinstance(deals['deal'], int):

                    total += shopping_list[item] // deals['quantity'] * deals["deal"]
                    shopping_list[item] = shopping_list[item] % deals['quantity']

                # else is an item deal => delete item with deal on it from the list
                else:

                    if deals['deal'] in shopping_list:

                        shopping_list[deals['deal']] -= shopping_list[item] // deals['quantity']

                        # make sure you don't delete more items than items in the shopping list
                        if shopping_list[deals['deal']] < 0:
                            shopping_list[deals['deal']] = 0

    # calculate the total for items with no deal
    for item in shopping_list:
        total += shopping_list[item] * prices[item]

    return total
