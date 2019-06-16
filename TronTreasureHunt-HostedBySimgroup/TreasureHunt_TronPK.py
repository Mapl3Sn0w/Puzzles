from coincurve import PrivateKey
import hashlib
import base58
import sha3
from itertools import chain, product
from random import sample

_numbers = '0123456789'
_hexdigits = '0123456789abcdef'
TronAddy = 'TF8PW7U9JDk88ivKMgzi5agHnfDbWmskEo'

#####################################################################################################
#THANKS TO @ARPOXY FOR PROVIDING THIS PART OF THE CODE FOR THE PRIVATE KEY TO ADDRESS TRANSFORMATION#
#####################################################################################################
def publickeyToAddress(publ):
    h = b'\x41' + sha3.keccak_256(publ).digest()[-20:]
    c = hashlib.sha256(hashlib.sha256(h).digest()).digest()[:4]
    return base58.b58encode(h+c)

def privatekeyHexToAddress(priv):
    pk = PrivateKey.from_hex(priv)
    publ = pk.public_key.format(compressed=False)[1:]
    return publickeyToAddress(publ)
#####################################################################################################
#THANKS TO @ARPOXY FOR PROVIDING THIS PART OF THE CODE FOR THE PRIVATE KEY TO ADDRESS TRANSFORMATION#
#####################################################################################################

def brute(length=1, hexdigits=True,numbers=True):
    
    choices = ''
    choices += _hexdigits if hexdigits else ''
    choices += _numbers if numbers else ''
    choices = ''.join(sample(choices, len(choices)))

    return (
        ''.join(candidate) for candidate in chain.from_iterable(product(choices,repeat = i) for i in range(length, length + 1)))

BruteChars = list(brute(2,True,False))
BruteNumber = list(brute(2,False,True))

SolArray = ['' for i in range(64)]

for Char in BruteChars:
    for Num in BruteNumber: 
        SolArray[0]='5'
        SolArray[1]='d'
        SolArray[2]='8'
        SolArray[3]='8'
        SolArray[4]='c'
        SolArray[5]='b'
        SolArray[6]='6'
        SolArray[7]='9'
        SolArray[8]='c'
        SolArray[9]='5'
        SolArray[10]='d'
        SolArray[11]='e'
        SolArray[12]='d'
        SolArray[13]=Char[0]
        SolArray[14]='8'
        SolArray[15]='d'
        SolArray[16]=Num[0]
        SolArray[17]='f'
        SolArray[18]='4'
        SolArray[19]='d'
        SolArray[20]='1d'
        SolArray[21]='5'
        SolArray[22]='5'
        SolArray[23]='5'
        SolArray[24]='1'
        SolArray[25]='f'
        SolArray[26]='e'
        SolArray[27]='5'
        SolArray[28]='6'
        SolArray[29]='2'
        SolArray[30]='5'
        SolArray[31]='d'
        SolArray[32]='2'
        SolArray[33]='c'
        SolArray[34]=Num[0]
        SolArray[35]='1'
        SolArray[36]='1'
        SolArray[37]='8'
        SolArray[38]='6'
        SolArray[39]='3'
        SolArray[40]='9'
        SolArray[41]='e'
        SolArray[42]='c'
        SolArray[43]='7'
        SolArray[44]='a'
        SolArray[45]='e'
        SolArray[46]=Num[0]
        SolArray[47]='0'
        SolArray[48]='4'
        SolArray[49]='8'
        SolArray[50]='e'
        SolArray[51]=Num[1]
        SolArray[52]='a'
        SolArray[53]='5'
        SolArray[54]='3'
        SolArray[55]='f'
        SolArray[56]='5'
        SolArray[57]=''
        SolArray[58]='e'
        SolArray[59]='2'
        SolArray[60]=Char[1]
        SolArray[61]='5'
        SolArray[62]='9'
        SolArray[63]='f'
        
        SolString = ''.join(SolArray)
        SolAddy = privatekeyHexToAddress(SolString).decode("utf-8")
        
        if SolAddy == 'TF8PW7U9JDk88ivKMgzi5agHnfDbWmskEo':
            print(SolString)