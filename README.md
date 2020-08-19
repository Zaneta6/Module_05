# Module_05
Module 5 of the Python bootcamp (tasks)

# BaseContact.py
is a simple card holder providing a parent class BaseContact() and a child class BusinessContact().
BaseContact() class refers to first name, last name, phone number and an e-mail address.
Additionally, there is also self._label_length variable to enable calculation of the label length (first name, space and last name).
Apart from the basic methods (__init__, __str__ and __repr__) it contain also the contact() method which refers to the phone number and first and last names.

# BusinessContact.py
contains a code for a child class (BusinessContact()) of the BaseContact() parent class.
Apart from all the parameters and methods of the parent class, BusinessContact() class contains additionally info about a position, company name and a business phone number.

# Main.py
contains the create_contact() function, which allows creating fake contacts both for BaseContact.py and BusinessContact.py using Python Faker.
