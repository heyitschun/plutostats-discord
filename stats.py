from client import client
from constants import addresses
from contracts import contract
from helpers import parse_token_url
from http_requests import send, get

def get_sold() -> int:
    sold = contract.functions.totalSupply().call()
    if not isinstance(sold, int):
        return 0
    return sold

async def get_adjusted_total_supply() -> int:
    ats = contract.functions.adjustedTotalSupply().call()
    if not isinstance(ats, int):
        return 1
    return ats

async def get_current_reserve() -> int:
    reserve = client.eth.get_balance(addresses["CATS_RESERVE"])
    if not isinstance(reserve, int):
        return 0
    return reserve

async def get_book_per_cat() -> float:
    current_reserve = await get_current_reserve()
    current_supply = await get_adjusted_total_supply()
    book_value_per_cat = current_reserve / current_supply
    return book_value_per_cat

async def get_quit_plus_royalties() -> float:
    tokens = [addresses["BLURETH_CONTRACT"], addresses["WETH_CONTRACT"]]
    book = await get_book_per_cat()
    current_supply = await get_adjusted_total_supply()
    royalties = 0
    for token in tokens:
        try:
            u = parse_token_url(addresses["CATS_RESERVE"], token)
            response = await send(get, u)
            data = response.json()
            if data.get("status") == "1" and "result" in data:
                royalties += int(data["result"])
            else:
                print(f"pass")
        except Exception as e:
            print(f"exception: {e}")
            royalties += 0
    print(f"royalties: {royalties}")
    total_quit = book + (royalties / current_supply)
    return total_quit