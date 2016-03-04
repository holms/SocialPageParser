import rethinkdb as rdb
import facebook
import json
import sys

fb_token = "1181287251898488|gIgRyNhd3trVLFE2A66mIhBFlp8"

class fb_event_collect:

    def __init__(self, **kwargs):
        self.init_rdb(self, kwargs)

    def init_fb(self, **kwargs):
        """Constructor for facebook sdk"""

        try:
            self.graph = facebook.GraphAPI(access_token=fb_token, version='2.4')
        except Exception as e:
            sys.exit(str(e))

    def init_rdb(self, **kwargs):
        """Constructor for rethinkdb"""

        self.rdb_host = kwargs['rdb_host']
        self.rdb_port = kwargs['rdb_port']
        self.rdb_db = kwargs['rdb_db']
        self.rdb_table = kwargs['rdb_table']

        try:
            rdb.connect(self.rdb_host, self.rdb_port),repl()
            rdb.db(self.rdb_db).tableCreate(self.rdb.table)
        except Exception as e:
            sys.exit(str(e))


    def save_event(self, data):
        """Save event to database"""
        rdb.table(self.rdb_table).insert([])


    def get_events(self):
        """Iterate through all events pages"""

        url = '/v2.4/'+self.page_id+'/events'
        data = self.graph.request(url)

        while 'next' in data['paging'].keys():
            print data['paging']['next']
            data = self.graph.request(url, args={
                        'limit' : 100,
                        'after' : data['paging']['cursors']['after']
            })

        return data



