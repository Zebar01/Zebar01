import os
import asyncio
from aiohttp import web

import urllib.request as req
from urllib import parse
import json

loop = asyncio.get_event_loop()

app = web.Application(loop=loop)


async def get_data(request):
    r = req.urlopen("https://api.telegram.org/bot836692378:********************************/getUpdates")

    data = r.read()
    data = data.decode('unicode-escape')
    return web.json_response(json.loads(data))

async def set_message(request):
    data = await request.post()
    text = data.get('text')
    chat_id = data.get('chat_id')

    msg_obj = {"chat_id": 491783309, "text": "My respect!"}
    msg_parse = parse.urlencode(msg_obj).encode('utf-8')

    result = req.urlopen("https://api.telegram.org/bot836692378:************************************/sendMessage", msg_parse)
    resp = result.read()
    resp = resp.decode('unicode-escape')
    return web.json_response(json.loads(resp))


app.router.add_route(method='GET', path='/get', handler=get_data, name='get')
app.router.add_route(method='POST', path='/set', handler=set_message, name='set')



web.run_app(app, host="0.0.0.0", port=os.environ.get("PORT") or 8080) 
