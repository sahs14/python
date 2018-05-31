import math

ad_dealList = []
ad_discountList = []
#Default pricing Rules
priceList = {'classic': 269.99, 'standout': 322.99, 'premium': 394.99}

#CustomerDeal  class to handle deal given in the initalize_referential_data
class CustomerDeals:
    def __init__(self, customer_name, ad_name, input_item, output_item):
        self._customerName = customer_name
        self._adName = ad_name
        self._inputItem = input_item
        self._outputItem = output_item

    def get_customer_name(self):
        return self._customerName

    def get_input_item(self):
        return self._inputItem

#CustomerDiscount  class to handle deal given in the initalize_referential_data
class CustomerDiscount:
    def __init__(self, customer_name, ad_name, price, count):
        self._customerName = customer_name
        self._adName = ad_name
        self._price = price
        self._count = count

    def get_customer_name(self):
        return self._customerName

    def get_price(self):
        return self._price
    
    def get_count(self):
        return self._count

#Privileged customers pricing rules
def initalize_referential_data():
    ad_dealList.append(CustomerDeals("SecondBite", "Classic Ads", 3, 2))
    ad_dealList.append(CustomerDeals("MYER", "Classic Ads", 5, 4))
    ad_discountList.append(CustomerDiscount("Axil Coffee Roasters", "Standout Ads", 299.99, 0))
    ad_discountList.append(CustomerDiscount("MYER", "Standout Ads", 309.99, 0))
    ad_discountList.append(CustomerDiscount("JORA", "Premium Ads", 379.99, 4))

