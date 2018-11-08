import os
from aiohttp import web
from datetime import datetime
import requests
import json

async def handle(request):
    name = request.match_info.get('name', "")
    url=f"http://back:8080/{name}"
    #url=f"http://"+os.environ['WS_BACK']+":8080/{name}"
    response = requests.get(url)
    if (response.ok):
        json_data = json.loads(response.content)
        resp = f"""
        You called at : {json_data['time']} (dynamic)
        On environment : {json_data['environment']} (from env variable)
        With path : {json_data['result']}   (from path)
        """
    
    return web.Response(text=resp)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app, port=os.environ['APP_PORT'])
