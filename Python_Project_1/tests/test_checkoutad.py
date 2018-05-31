import checkout
import referentialData

def test_defaultcustomer():
    referentialData.initalize_referential_data()
    c3 = checkout.CheckOut("default")
    c3.add("classic")
    c3.add("standout")
    c3.add("premium")
    #print("Total value for deafult Customer:{0}".format(c3.total()))
    assert c3.total() == 987.97

def test_jora():
    referentialData.initalize_referential_data()
    c4 = checkout.CheckOut("JORA")
    c4.add("premium")
    c4.add("premium")
    c4.add("premium")
    c4.add("premium")
    #print("Total value for deafult Customer:{0}".format(c3.total()))
    assert c4.total() == 1519.96