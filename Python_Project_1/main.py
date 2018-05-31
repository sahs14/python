import checkout
import referentialData

def main():
    referentialData.initalize_referential_data()
    """customer_name = input("secondBites")
    c1 = checkout.CheckOut(customer_name)
    c1.add("classic")
    c1.add("classic")
    c1.add("classic")
    c1.add("premium")
    print("Total value for SecondBite Customer:{0}".format(c1.total()))"""

    """c2 = checkout.CheckOut("Axil Coffee Roasters")
    c2.add("standout")
    c2.add("standout")
    c2.add("standout")
    c2.add("premium")
    print("Total value for Axil Coffee Roasters Customer:{0}".format(c2.total()))

    c3 = checkout.CheckOut("default")
    c3.add("classic")
    c3.add("standout")
    c3.add("premium")
    print("Total value for deafult Customer:{0}".format(c3.total()))

    c4 = checkout.CheckOut("Jora")
    c4.add("premium")
    c4.add("premium")
    c4.add("premium")
    c4.add("premium")
    print("Total value for Jora Customer:{0}".format(c4.total()))

    c5 = checkout.CheckOut("MYER")
    c5.add("classic")
    c5.add("classic")
    c5.add("classic")
    c5.add("classic")
    c5.add("classic")
    c5.add("classic")
    c5.add("standout")
    c5.add("standout")
    c5.add("premium")
    print("Total value for MYER Customer:{0}".format(round(c5.total(),3)))

    c6 = checkout.CheckOut("MYER")
    c6.add("classic")
    c6.add("standout")
    c6.add("standout")
    c6.add("premium")
    print("Total value for MYER Customer:{0}".format(c6.total()))

    c7 = checkout.CheckOut("MYER")
    c7.add("classic")
    c7.add("classic")
    c7.add("classic")
    c7.add("classic")
    c7.add("classic")
    c7.add("classic")
    c7.add("classic")
    c7.add("classic")
    c7.add("classic")
    c7.add("classic")
    c7.add("standout")
    c7.add("standout")
    c7.add("premium")
    print("Total value for MYER Customer:{0}".format(round(c7.total(),3)))

    c8 = checkout.CheckOut("SecondBite")
    c8.add("classic")
    c8.add("classic")
    c8.add("classic")
    c8.add("classic")
    c8.add("classic")
    c8.add("classic")
    c8.add("premium")
    print("Total value for SecondBite Customer:{0}".format(c8.total()))

    c9 = checkout.CheckOut("SecondBite")
    c9.add("classic")
    print("Total value for SecondBite Customer:{0}".format(c9.total()))

    c10 = checkout.CheckOut("FlipKart")
    c10.add("premium")
    print("Total value for FlipKart Customer:{0}".format(c10.total()))

    c11 = checkout.CheckOut("Axil Coffee Roasters")
    c11.add("standout")
    print("Total value for Axil Coffee Roasters Customer:{0}".format(c11.total()))"""
    
    c4 = checkout.CheckOut("JORA")
    c4.add("premium")
    c4.add("premium")
    c4.add("premium")
    c4.add("premium")
    print("Total value for deafult Customer:{0}".format(c4.total()))

if __name__ == "__main__":
    main()