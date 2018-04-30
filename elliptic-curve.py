#!/usr/bin/python3
import math
import random


class Private:
    def __init__(self, public_big_prime, public_generator):
        # between 1 and Public's big prime
        self.public_big_prime = public_big_prime
        self.public_generator = public_generator
        self.__private_key = random.randint(0, self.public_big_prime)

    def users_shared_secret(self, CURVE_OBJ):
        self.users_shared_secret = (CURVE_OBJ.feed_curve(self.__private_key*self.public_generator)) % self.public_big_prime
        return self.users_shared_secret

    def group_shared_secret(self, other_users_shared_secret):
        return (self.users_shared_secret * other_users_shared_secret) % self.public_big_prime


class Curve25519:
    def __init__(self):
        pass

    def feed_curve(self, generator):
        # y^2 = x^3 + 486662x^2 + x
        return (generator ** 3) + (486662 * generator ** 2) + generator


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
g = Server.get_generator()
n = Server.get_prime()

Alice = Private(n, g)
Bob = Private(n, g)
ECDH = Curve25519()

ag = Alice.users_shared_secret(ECDH)
bg = Bob.users_shared_secret(ECDH)

bga = Alice.group_shared_secret(bg)
agb = Bob.group_shared_secret(ag)
print(bga)
print(agb)