from sanic import Sanic, Blueprint
from sanic.response import json
import os

app = Sanic(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/<path:path>', methods=["GET", "POST"])
async def catch_all(request, path=''):
    print(path, request.json)
    return json({})

@app.websocket("/ws")
async def handler(request, ws):
    print(request.json)
    while True:
        message = await ws.recv()
        print(message)