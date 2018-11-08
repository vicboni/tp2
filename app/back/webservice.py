import os
from aiohttp import web
from datetime import datetime

async def handle(request):
    name = request.match_info.get('name', "Here is the root")
    data = {
            'time': str(datetime.now()),
            'environment': os.environ['ENVIRONMENT'],
            'hostname': os.uname()[1],
            'result': name
            }
    return web.json_response(data)

async def write_to_file(request):
    something = request.match_info.get('something', "")

    print(something)
    if something:
        with open('logs/my-messages.log', 'a') as the_file:
            the_file.write(f"{something}\n")
    else:
        return web.Response(status=500)

    return web.Response(status=200)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle),
                web.get('/write/{something}', write_to_file)])

web.run_app(app)
