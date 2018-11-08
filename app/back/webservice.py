import os
from aiohttp import web
from datetime import datetime

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    data = {
            'time': str(datetime.now()),
            'environment': os.environ['ENVIRONMENT'],
            'result': name
            }
    return web.json_response(data)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app)
