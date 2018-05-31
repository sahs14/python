import referentialData
import math

# Cart class to handle the mapping between item List and customer Name. 
# check of deal and discount for the customer mapped in referential_data and calculate the total
class Cart:
    def __init__(self, name, item_list=None):
        self.customer_name = name
        if item_list is None:
            item_list = []
        self.itemInfo = item_list

    def check_deal(self,count_classic):
        deal = 0.0
        for deal_info in referentialData.ad_dealList:
            if deal_info.get_customer_name() == self.customer_name:
                if count_classic != 0:
                    if count_classic >= deal_info.get_input_item():
                        deal = math.floor(count_classic / deal_info.get_input_item())
        return count_classic - deal

    def check_discount(self,total_standard,count_standard,total_premium,count_premium):
        discount_price = 0.0
        for discount in referentialData.ad_discountList:
            if discount.get_customer_name() == self.customer_name:
                if count_standard >= discount.get_count() :
                    discount_price = discount.get_price() * count_standard
                    discount_price = total_standard - discount_price   
                else :
                    if count_premium >= discount.get_count() :
                        discount_price = discount.get_price() * count_premium
                        discount_price = total_premium - discount_price
        return discount_price

    def total_price(self):
        total_classic_price = 0.0
        total_standard_price = 0.0
        total_premium_price = 0.0
        total = 0.0
        count_classic = self.itemInfo.count('classic')
        count_standard = self.itemInfo.count('standout')
        count_premium = self.itemInfo.count('premium')

        count_classic = 0 if count_classic == 0 else self.check_deal(count_classic)

        total_classic_price = referentialData.priceList['classic'] * int(count_classic)

        total_premium_price += referentialData.priceList['premium'] * count_premium

        total_standard_price += referentialData.priceList['standout'] * count_standard

        total = total_premium_price + total_standard_price + total_classic_price
        discount_price = 0.0
        discount_price = self.check_discount(total_standard_price,count_standard,total_premium_price,count_premium)

        return total - discount_price



class CheckOut:
    def __init__(self, customer_name):
        self.name = customer_name
        self.itemList = []

    def add(self, item):
        self.itemList.append(item)

    def total(self):
        cart_item = Cart(self.name, self.itemList)
        return cart_item.total_price()
