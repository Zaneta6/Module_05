import sys
import logging
logging.basicConfig(level=logging.INFO)
from faker import Faker
fake = Faker()
from Main import create_contact
from BaseContact import BaseContact

contacts = []

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
    
    @property
    def label_length(self):
        return self._label_length
    @label_length.setter
    def label_length(self, label_length):
        return self._label_length + len(self.first_name, ' ', self.last_name)

    def __str__(self):
        return "Name: {} {} {} Company: {} {} Position: {} {} Business phone no: {} {} e-mail: {} {} label length: {}".format(self.first_name, self.last_name, '\t', self.company, '\t', self.position, '\t', self.business_phone, '\t', self.email, '\t', self._label_length)
    def __repr__(self):
        return f"{self.first_name}, {self.last_name}, {self.company}, {self.position}, {self.business_phone}, {self.email}, {self._label_length}"
    def contact(self, first_name, last_name):
        logging.info("Dialing {} and calling {} {}".format(self.business_phone, self.first_name, self.last_name))
    create_contact("business", number=0)
