import sys
import logging
logging.basicConfig(level=logging.INFO)


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
    
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

    def contact(self):
        logging.info("Dialing {} and calling {} {}".format(self.phone_number, self.first_name, self.last_name))
