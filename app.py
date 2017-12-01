'''

第一个python web

'''
import asyncio
import os
import json
import time
import logging
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)

def index(request):
    """返回主页
    
    这个方法用来返回主页页面
    
    Arguments:
        request {request} -- 具体的请求信息
    
    Returns:
        web.Response() -- 服务器发出的回复
    """
    
    return web.Response(body=b'<h1>HelloWorld!</h1>',content_type='text/html')


@asyncio.coroutine
def init(loop):
    """上帝进程
    
    webapp的第一个进程
    
    Decorators:
        asyncio
    
    Arguments:
        loop {asyncio event loop} -- 一个asyncio的事件循环
    
    Yields:
        server -- 一个监听9000端口的web服务
    """
    
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
