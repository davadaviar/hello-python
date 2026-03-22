def apply_discount(price, discount):
    is_price = type(price) == int or type(price) == float
    is_discount = type(discount) == int or type(discount) == float

    # check if price and discount are numbers
    if not is_price:
        return 'The price should be a number'
    if not is_discount:
        return 'The discount should be a number'

    # check if price lower than 0
    if price <= 0:
        return 'The price should be greater than 0'

    # check if discount between 0 and 100
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'

    # calculate the discounted price
    discount_price = price * (1 - discount / 100)

    # calculate final price
    final_price = round(discount_price, 2)

    return final_price

print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(100, 100))
print(apply_discount(74.5, 20.0))