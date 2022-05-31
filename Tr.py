import ecdsa
import base58
import requests
from Crypto.Hash import keccak
from tronpy.keys import PrivateKey
import colorama
from colorama import Fore, Back, Style
from bitcoinaddress import Wallet
colorama.init()


print("Please Wait...")

a = 1
b = 2
c = 100
count=0
remaining=c-b
F = []
P = b
while P<c:
    count+= 1
    ran= P
    HEX = "%064x" % ran
    priv_key = PrivateKey(HEX)
    print(priv_key)
