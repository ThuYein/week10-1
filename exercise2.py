import random

__author__ = 'Lindsay Ward'
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0

def format_currency(price):
   return "${:,.2f}".format(price)

price = INITIAL_PRICE

while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    ran = random.randint(1, 2)
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if ran == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        priceChange = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + priceChange)
    #print("${:,.2f}".format(price))
    print format_currency(price)
