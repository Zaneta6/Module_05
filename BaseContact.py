import sys
import logging
logging.basicConfig(level=logging.INFO)
from faker import Faker
fake = Faker()
from Main import create_contact

contacts = []

# Construct the BaseContact() class to define a basic contact representation for a card holder.
# It contains: first name, last name, phone number and e-mail.
# Additionally, there is also self._label_length variable for calculation of the label length (first name, space and last name).
# Apart from the basic methods (__init__, __str__ and __repr__) it contains also contact() method defined in the main.py file.
class BaseContact():
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        #Variables:
        self._label_length = 0
    
    @property
    def label_length(self):
        return self._label_length
    @label_length.setter
    def label_length(self, label_length):
        return self._label_length + len(self.first_name, ' ', self.last_name)

    def __str__(self):
        return "Name: {} {} {} phone no: {} {} e-mail: {} {} label length: {}".format(self.first_name, self.last_name, '\t', self.phone_number, '\t', self.email, '\t', self._label_length)
    def __repr__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_number}, {self.email}, {self._label_length}"
    def contact(self, first_name, last_name):
        logging.info("Dialing {} and calling {} {}".format(self.phone_number, self.first_name, self.last_name))
    create_contact("base", number=0)
