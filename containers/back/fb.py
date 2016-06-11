from datetime import datetime
import falcon
import json
import facebook
import requests

import config
import utils as u
from db import db


graph = facebook.GraphAPI(access_token=config.fb_token, version='2.4')

class FbEvents:

    cache_expiration_time = None

    def __init__(self, **kwargs):
        self.db = db()
        self.table = "events"

    def _check_last_access(self, page_id):
        """Check for last access time, and return false, if less than x minutes

           Keyword arguments:
           page_id - Facebook page ID
        """

        last_access = self.db.get_last_access(page_id+"_events")

        if last_access:
            elapsed_time = last_access - datetime.now()
            elapsed_minutes = round( elapsed_time.total_seconds() / 60)
            if elapsed_minutes > config.fb_timeout_events:
                return True # Allow API call

        self.cache_expiration_time = elapsed_time.total_seconds()
        return False # Deny API call


    def _save_last_access(self, page_id):
        """Save last access time"

           Keyword arguments:
           page_id - Facebook page ID
        """
        self.db.set_last_access(page_id+"_events")

    def _request_events(self, page_id):
        """Request events and save to database

           Keyword arguments:
           page_id - Facebook page ID
        """
        try:
            data = graph.request('/v2.4/'+page_id+'/events')
            resp.status = falcon.HTTP_200
        except Exception as e:
            data = {'error': str(e)}

        self.db.save_items(
            { "id" : page_id, "data": data },
            self.table
        )

    def on_get(self, req, resp, page_id):
        """Get request

           Keyword arguments:
           req - HTTP request
           resp - HTTP response
           page_id - Faceboook page ID
        """

        if self._check_last_access(page_id):
            self._request_events(page_id)
            self._save_last_access(page_id)

        else:
            data = self.db.get_items(page_id, self.table)

        # Remove pagination dict
        del(data['pages'])

        # Add expiration cache time in seconds
        data['cache_expiration_time'] = self.cache_expiration_time

        resp.body = u.jdump(data)

class FbPosts:

    def _get_posts(self, page_id):
        """Get Facebook posts

        Keyword arguments:
            page_id - Facebook page ID
        """
        try:
            data = graph.request('/v2.4/'+page_id+'/posts', args={'limit': 100})
            resp.status = falcon.HTTP_200
        except Exception as e:
            data = {'error': str(e)}

        return json.dumps(data)

    def on_get(self, req, resp, page_id):
        """Get request

           Keyword arguments:
           req - HTTP request
           resp - HTTP response
           page_id - Faceboook page ID
        """

        resp.body = self._get_posts(page_id)

