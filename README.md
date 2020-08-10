# Module_05
Module 5 of the Python bootcamp (tasks)

# Contacts.py
is a simple card holder providing a parent class BaseContact() and a child class BusinessContact().
BaseContact() class refers to first name, last name, phone number and an e-mail address.
BusinessContact() class contains additionally information about a position, company name and a business phone number.
Additionally, there is also self.label variable, which calculates the length of the label (first name, space and last name).
Apart from the basic methods (__init__, __str__ and __repr__) both classes contain also the contact() method which refers to the phone number and first and last names.
Functions cont_gen_base() and cont_gen_business() allow generating a given number of fake contacts of both classes using Python Faker library.
