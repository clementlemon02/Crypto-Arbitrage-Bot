import aiohttp
from config import PUB_URL, HEADERS

async def fetch(session, url, params=None):
    """Asynchronously fetch data from the API."""
    async with session.get(url, headers=HEADERS, params=params) as response:
        if response.status == 200:
            return await response.json()
        else:
            print(f"Failed to fetch {url} (Status {response.status})")
            return None

async def get_all_exchanges(session):
    """Retrieve all available exchanges asynchronously."""
    endpoint = "/exchanges"
    params = {"per_page": 250, "page": 1}
    data = await fetch(session, PUB_URL + endpoint, params)
    if data:
        return [ex["id"] for ex in data]
    return []

async def get_exchange_tickers(session, exchange_id):
    """Fetch all trading pairs for a given exchange asynchronously, filtering for USDT/USDC pairs."""
    data = await fetch(session, f"{PUB_URL}/exchanges/{exchange_id}/tickers")
    if data and "tickers" in data:
        return [
            {
                "exchange": exchange_id,
                "pair": f"{t['base']}/{t['target']}",
                "base": t["base"],
                "target": t["target"],
                "price": t["last"],
                "volume": t["volume"]
            }
            for t in data["tickers"]
            if t["last"] is not None and t["target"] in ["USDT", "USDC"]
        ]
    return []
