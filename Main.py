from faker import Faker
fake = Faker()
import logging
logging.basicConfig(level=logging.INFO)

# Create empty lists for contacts
contacts = []

# Define the method that generates a given number of contacts of a given type (base or business) using a Faker library
def create_contact(contact_type, number):
    for _ in range(0, number):
        if contact_type == "base":
            return contacts.append((fake.first_name(), fake.last_name(), fake.phone_number(), fake.safe_email()))
        elif contact_type == "business":
            return contacts.append((fake.job(), fake.company(), fake.phone_number(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.safe_email()))
        else:
            logging.info("Incorrect contact type (choose base or business) or number of contacts")
            