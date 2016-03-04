import falcon
import json

import fb

api = falcon.API()

api.add_route('/{page_id}/events', fb.FbEvents())
api.add_route('/{page_id}/posts', fb.FbPosts())

app = application = api

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
