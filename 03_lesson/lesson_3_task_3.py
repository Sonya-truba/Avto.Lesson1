from address import Address
from mailing import Mailing
address1 = Address("23456", "kazan", "ktybyf", 4, 34)
address2 = Address("23456", "kazan", "ktybyf", 4, 34)
cost = 1234567
track = 12345
my_mailing1 = Mailing(address1, address2, cost, track)
my_mailing1.myLetter()
