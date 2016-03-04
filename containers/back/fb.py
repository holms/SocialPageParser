import falcon
import json
import rethinkdb as rdb
import facebook
import requests

import config

graph = facebook.GraphAPI(access_token=config.fb_token, version='2.4')

class FbEvents:

    def on_get(self, req, resp, page_id):

        try:
            data = graph.request('/v2.4/'+page_id+'/events')
            resp.status = falcon.HTTP_200
        except Exception as e:
            data = {'error': str(e)}

        resp.body = json.dumps(data)

        """
        try:
            rdb.connect(config.rethinkdb_host, config.rethinkdb_port).repl()
            data = { 'info': 'success'}
        except Exception as e:
            data = { 'error': str(e) }
        """

class FbPosts:

    def on_get(self, req, resp, page_id):

        try:
            data = graph.request('/v2.4/'+page_id+'/posts', args={'limit': 100})
            resp.status = falcon.HTTP_200
        except Exception as e:
            data = {'error': str(e)}

        resp.body = json.dumps(data)

