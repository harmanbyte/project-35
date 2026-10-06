#Problem1

"""
Simple Bill Splitter for beginners.
Enter number of people, enter either a single bill or each person's items,
enter tip percent, optionally add VAT, and get a neat per-person total.
"""

import sys

def get_float(prompt):
    """This gets a positive float from user"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")

def get_int(prompt):
    """Safely get a positive integer."""
    while True: