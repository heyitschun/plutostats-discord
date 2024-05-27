import discord
import asyncio
from discord.ext import commands, tasks
from helpers import format_quit_price
from stats import get_book_per_cat, get_quit_plus_royalties
from env_vars import DISCORD_CLIENT_TOKEN, QUIT_CHANNEL_ID, QR_CHANNEL_ID

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    update_channel_names.start()

@tasks.loop(minutes=20)
async def update_channel_names():
    quit_channel = bot.get_channel(QUIT_CHANNEL_ID)
    royalties_channel = bot.get_channel(QR_CHANNEL_ID)
    
    quit_price = await get_book_per_cat()
    formatted_quit_price = format_quit_price(quit_price)

    quit_plus_price = await get_quit_plus_royalties()
    formatted_royalties_price = format_quit_price(quit_plus_price)
    
    if quit_channel:
        new_quit_price_name = f"Quit Price: {formatted_quit_price} ETH"
        new_royalties_name = f"Plus Royalties: {formatted_royalties_price} ETH"
        try:
            await quit_channel.edit(name=new_quit_price_name)
            print(f'Royalties renamed to {new_quit_price_name}')
        except discord.errors.RateLimited as e:
            retry_after = e.retry_after
            print(f'Rate limited. Retrying in {retry_after:.2f} seconds.')
            await asyncio.sleep(retry_after)
        except discord.errors.HTTPException as e:
            print(f'HTTP exception: {e}')
        except Exception as e:
            print(f'Unexpected error: {e}')
        
        try:
            await royalties_channel.edit(name=new_royalties_name)
            print(f'Royalties renamed to {new_royalties_name}')
        except discord.errors.RateLimited as e:
            retry_after = e.retry_after
            print(f'Rate limited. Retrying in {retry_after:.2f} seconds.')
            await asyncio.sleep(retry_after)
        except discord.errors.HTTPException as e:
            print(f'HTTP exception: {e}')
        except Exception as e:
            print(f'Unexpected error: {e}')

        

@update_channel_names.before_loop
async def before_update_channel_name():
    await bot.wait_until_ready()

bot.run(DISCORD_CLIENT_TOKEN)