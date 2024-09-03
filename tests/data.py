import random
import string

def generate_email():
    return f"user{random.randint(10000, 99999)}@example.com"