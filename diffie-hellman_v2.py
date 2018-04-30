#!/usr/bin/python3
# Diffie-Helman implementation
import random

class Private:
    def __init__(self, public_big_prime, public_generator):
        # between 1 and Public's big prime
        self.public_big_prime = public_big_prime
        self.public_generator = public_generator
        self.__private_key = random.randint(0, self.public_big_prime)
    
    def get_public_component(self):
        return (self.public_generator ** self.__private_key) % self.public_big_prime

    def manipulate_others_public_component(self, others_public_mix):
        return (others_public_mix ** self.__private_key) % self.public_big_prime


class Public:
    def __init__(self):
        # g - small prime
        self.public_generator = 13
        # n - big - ~4000 bits - this is the modulo number (should be large)
        self.public_big_prime = 1290823

    def get_generator(self):
        return self.public_generator

    def get_prime(self):
        return self.public_big_prime


Server = Public()
Alice = Private(Server.get_prime(), Server.get_generator())
Bob = Private(Server.get_prime(), Server.get_generator())

# Discrete log
ag = Alice.get_public_component()
bg = Bob.get_public_component()

bga = Alice.manipulate_others_public_component(bg)
agb = Bob.manipulate_others_public_component(ag)

print(f'Alice has a mix of: {bga}\nBob has a mix of: {agb}')
