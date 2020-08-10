import sys
import logging
logging.basicConfig(level=logging.INFO)
from faker import Faker
fake = Faker()

# Construct the BaseContact() class to define a basic contact representation for a card holder.
# It contains: first name, last name, phone number and e-mail.
# Additionally, there is also self.label variable, which calculates the length of the label (first name, space and last name).
# Apart from the basic methods (__init__, __str__ and __repr__) it contains also contact() method.
class BaseContact():
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        #Variables:
        self.label = len(first_name + last_name + ' ')
    def __str__(self):
        return "Name: {} {} {} phone no: {} {} e-mail: {} {} label length: {}".format(self.first_name, self.last_name, '\t', self.phone_number, '\t', self.email, '\t', self.label)
    def __repr__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_number}, {self.email}, {self.label}"
    def contact(self.first_name, self.last_name):
        logging.info("Dialing {} and calling {} {}".format(self.phone_number, self.first_name, self.last_name))

# Construct the BusinessContact() class to define a child class (business) contact representation for a card holder.
# It contains: all the parent class parameters plus a position and a company name as well as a business phone number.
# Additionally, there is also self.label variable, which calculates the length of the label (first name, space and last name).
# Apart from the basic methods (__init__, __str__ and __repr__) it contains also contact() method.
class BusinessContact(BaseContact):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone
    def __str__(self):
        return "Name: {} {} {} Company: {} {} Position: {} {} Business phone no: {} {} e-mail: {} {} label length: {}".format(self.first_name, self.last_name, '\t', self.company, '\t', self.position, '\t', self.business_phone, '\t', self.email, '\t', self.label)
    def __repr__(self):
        return f"{self.first_name}, {self.last_name}, {self.company}, {self.position}, {self.business_phone}, {self.email}, {self.label}"
    def contact(self.first_name, self.last_name):
        logging.info("Dialing {} and calling {} {}".format(self.business_phone, self.first_name, self.last_name))

# Create empty lists for base contacts (entries_base) and business contacts (entries_business)
entries_base = []
entries_business = []

# Define the method that generates a given number of base contacts using a Faker library
def cont_gen_base(number):
    for _ in range(0, number):
        entries_base.append(BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.safe_email()))
    return entries_base

# Define the method that generates a given number of business contacts using a Faker library
def cont_gen_business(number):
    for _ in range(0, number):
        entries_business.append(BusinessContact(fake.job(), fake.company(), fake.phone_number(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.safe_email()))
    return entries_business

cont_gen_base(5)
for base_entry in entries_base:
    print(base_entry)

cont_gen_business(5)
for business_entry in entries_business:
    print(business_entry)