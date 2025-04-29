from django.utils.text import slugify
from random import SystemRandom
import string

def random_letters(k=5):
    return ''.join(SystemRandom().choice(
        string.ascii_letters + string.digits, 
        k=k
    ))

def slugify_new(text, k=4):
    return slugify(text) + '-' + random_letters(k)