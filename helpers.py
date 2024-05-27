from env_vars import BLASTSCAN_API_KEY
from web3 import Web3

def to_eth(wei) -> float:
    return round(float(Web3.from_wei(wei, 'ether')),5)

def format_quit_price(quit_price) -> str:
    quit_price = f"{to_eth(quit_price):,.3f}"
    return quit_price

def parse_token_url(account_address, token_address) -> str:
    url = (
        f"https://api.blastscan.io/api?module=account&action=tokenbalance"
        f"&contractaddress={token_address}&address={account_address}"
        f"&tag=latest&apikey={BLASTSCAN_API_KEY}"
    )
    return url