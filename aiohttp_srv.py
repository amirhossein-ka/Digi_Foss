from aiohttp import web


async def hello(request):
    return web.Response(text="hello world")


myapp = web.Application()
myapp.add_routes([web.get('/', hello)])

