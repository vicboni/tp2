import os
from aiohttp import web
from datetime import datetime
import requests
import json

async def handle(request):
    name = request.match_info.get('name', "")

    #url=f"http://back:8080/{name}"
    url=f"http://{os.environ['WS_BACK_URL']}:8080/{name}"
    response = requests.get(url)
    if (response.ok):
        json_data = json.loads(response.content)
        resp = f"""
        You called at : {json_data['time']} (dynamic)
        On environment : {json_data['environment']} (from env variable)
        With path : {json_data['result']}   (from URL path)
        With front : {os.uname()[1]} (from real hostname of front service)
        With back  : {json_data['hostname']} (from real hostname of back service)
        """
    
    return web.Response(text=resp)

async def write_to_file(request):
    something = request.match_info.get('something', "")

    print(something)
    if something:
        resp=something

        url=f"http://{os.environ['WS_BACK_URL']}:8080/write/{something}"
        response = requests.get(url)
    else:
        resp="There is nothing to print"

    return web.Response(text=resp)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle),
                web.get('/write/{something}', write_to_file)])

web.run_app(app, port=os.environ['APP_PORT'])
