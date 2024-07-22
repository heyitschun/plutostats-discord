import discord
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

def check_permissions(bot,  channel_id: int) -> None:
    channel = bot.get_channel(channel_id)
    if channel:
        permissions = channel.permissions_for(channel.guild.me)
        permissions_list = [perm for perm, value in permissions if value]
        print(f"Permissions in {channel.name}: {', '.join(permissions_list)}\n")

        if isinstance(channel, discord.TextChannel):
            category = channel.category
            if category:
                category_permissions = category.permissions_for(channel.guild.me)
                category_permissions_list = [perm for perm, value in category_permissions if value]
                print(f"Permissions in category {category.name}: {', '.join(category_permissions_list)}\n")
    else:
        print(f"Channel with ID {channel_id} not found.")
