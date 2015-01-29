__author__ = 'RanadeepPolavarapu'

import string
import random

class pyStringUtils:

    """
    Useful string utilities available for public use.

    Created for use in Python 3.4. Should work for all Py3k versions.
    """
    def __init__(self):
        pass

    @staticmethod
    def string_subtraction(a, b):
        return ''.join(a.rsplit(b))

    @staticmethod
    def random_id_generator(size, chars=string.ascii_letters + string.digits):
        """
        Useful to generate random IDs, strings, passwords, etc.

        Uses alphabetical chars, numerical chars, whitespace, and punctuation to generate as specified below.

        Available 'chars' argument:
            string.ascii_letters - string.ascii_lowercase + string.ascii_uppercase
            string.ascii_lowercase - 'abcdefghijklmnopqrstuvwxyz'
            string.ascii_uppercase - 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            string.digits - '0123456789'
            string.hexdigits - '0123456789abcdefABCDEF'
            string.octdigits - '01234567'
        """
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def random_color_hex():
        r = lambda: random.randint(0, 255)
        return '#%02X%02X%02X' % (r(), r(), r())

    @staticmethod
    def convert_CamelCase_to_underscore(s):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    @staticmethod
    def convert_underscore_to_CamelCase(s):
        s = s.lower()
        return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), s)
