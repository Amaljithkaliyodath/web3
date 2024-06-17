

from web3 import Web3
import os
import stat

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/84214fe5e4d8451fb1d3cb5bc86699b0'))



account = w3.eth.account.create()


private_key = account.key.hex()
public_key = account.address


private_key_file = 'private_key.txt'
with open(private_key_file, 'w') as file:
    file.write(private_key)


os.chmod(private_key_file, stat.S_IREAD)


print(f'Public Key (Address): {public_key}')
