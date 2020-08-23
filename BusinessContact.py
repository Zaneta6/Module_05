import sys
import logging
logging.basicConfig(level=logging.INFO)
from BaseContact import BaseContact


# Construct the BusinessContact() class to define a child class (business) contact representation for a card holder.
# It contains: all the parent class parameters plus a position and a company name as well as a business phone number.
# Additionally, there is also self._label_length variable for calculation of the label length (first name, space and last name).
# Apart from the basic methods (__init__, __str__ and __repr__) it contains also contact() method defined in the main.py file.
class BusinessContact(BaseContact):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone
    
    def contact(self):
        logging.info("Dialing {} and calling {} {}".format(self.business_phone, self.first_name, self.last_name))
