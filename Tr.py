import ecdsa
import base58
import requests
from Crypto.Hash import keccak
from tronpy.keys import PrivateKey
import colorama
from colorama import Fore, Back, Style

colorama.init()


print("Please Wait...")

a = 1
while True:

    priv_key = PrivateKey.random(1,100,75)
    print(priv_key)   
