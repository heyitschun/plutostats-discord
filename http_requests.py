import httpx

async def get(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response

async def send(method, url):
    response = await method(url)
    return response