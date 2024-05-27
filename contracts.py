import json
from client import client
from constants import addresses
from web3.contract.contract import Contract

with open("./abi/PlutocatsTokenABI.json", "r") as f:
    PLUTOCATS_ABI = json.loads(f.read())
    
contract: Contract = client.eth.contract(address=addresses["CATS_CONTRACT"], abi=PLUTOCATS_ABI)