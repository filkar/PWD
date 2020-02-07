import random
import string

def generate(nbr):
    pwd = ''
    for _ in range(0, nbr, 1):
        pwd += random.choice(string.ascii_letters + string.digits + string.punctuation)

    print (pwd)
generate(10)
