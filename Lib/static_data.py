import random
import string


class User:
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    EMAIL = f'{random_string}@gmail.com'
    NAME = 'Bob'
    LASTNAME = 'Bobber'
    PASSWORD = random_string
    ADDRESS = 'Lincoln ave, 21'
    CITY = 'Springfield'
    ZIP_CODE = '42345'
    PHONE = '555-123456'
