from faker import Faker
fake = Faker()
import logging
logging.basicConfig(level=logging.INFO)
from BaseContact import BaseContact
from BusinessContact import BusinessContact


# Define the method that generates a given number of contacts of a given type (base or business) using a Faker library
def create_contact(contact_type, number):
    contacts = []
    for _ in range(0, number):
        if contact_type == "base":
            contacts.append(BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.safe_email()))
        elif contact_type == "business":
            contacts.append(BusinessContact(fake.job(), fake.company(), fake.phone_number(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.safe_email()))
        else:
            logging.info("Incorrect contact type (choose base or business) or number of contacts")
            return []
    return contacts

base_contacts = create_contact("base", 4)
business_contacts = create_contact("business", 4)


for business_contact in business_contacts:
    business_contact.contact()