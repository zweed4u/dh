#!/usr/bin/python3
# Super basic Diffie-Helman implementation
import random

class Private:
    def __init__(self):
        self.__private_key = int(random.random() * 10 ** 8)

    def mix_generator(self, generator):
        return self.__private_key * generator

    def take_mix_and_mix_more(self, other_user_mix):
        return self.__private_key * other_user_mix


class Public:
    def __init__(self):
        self.public_generator = 100
        self.public_big_prime = 37

    def get_generator(self):
        return self.public_generator

    def get_prime(self):
        return self.public_big_prime


Server = Public()
Alice = Private()
Bob = Private()

ag = Alice.mix_generator(Server.get_generator())
bg = Bob.mix_generator(Server.get_generator())

# shared secret
agb = Bob.take_mix_and_mix_more(ag)
bga = Alice.take_mix_and_mix_more(bg)

print(f'Alice has a mix of: {bga}\nBob has a mix of: {agb}')
