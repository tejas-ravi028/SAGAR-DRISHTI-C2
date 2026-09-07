import asyncio
import websockets
import json

async def test():
    print("Connecting to AISStream...")
    url = "wss://stream.aisstream.io/v0/stream"
    # Testing the Singapore Strait (guaranteed 50+ ships per second)
    payload = {
        "APIKey": "fa591306907526be7c2583c27123ea0662f79de2",
        "BoundingBoxes": [[[1.15, 103.60], [1.45, 104.10]]],
        "FilterMessageTypes": ["PositionReport"]
    }
    async with websockets.connect(url) as ws:
        await ws.send(json.dumps(payload))
        print("Connected! Listening for vessel packets...")
        msg = await asyncio.wait_for(ws.recv(), timeout=5.0)
        data = json.loads(msg)
        name = data.get("MetaData", {}).get("ShipName", "Unknown")
        print(f"SUCCESS! Ingested live vessel: {name}")

asyncio.run(test())
