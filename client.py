from web3 import Web3
from constants import BLAST_RPC_URLS

client = None

for rpc in BLAST_RPC_URLS:
    client = Web3(Web3.HTTPProvider(rpc))
    if client.is_connected():
        print(f"Connected to: {rpc}")
        break
    else:
        raise Exception("Failed to connect to any RPC")
