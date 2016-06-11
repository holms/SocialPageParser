import sys
import rethinkdb as rdb
from datetime import datetime

import config


class db:

    def __init__(self, **kwargs):
        self._init_rdb(config.rdb)

    def _init_rdb(self, kwargs):
        """Constructor for rethinkdb"""
        self.__dict__.update(kwargs)
        self.create_tables()

    def create_tables(self):
        """Create tables"""

        try:
            rdb.connect(self.host, \
               self.port).repl()

            for table in self.tables:
                if not rdb.db(self.db).table_list().contains(table).run():
                        rdb.db(self.db).table_create(table).run()

        except Exception as e:
            sys.exit(str(e))

    def get_item(self, uuid, table):
        return rdb.table(table).get(uuid).run()

    def get_items(self, data, table):
        """Get items from table"""
        return rdb.table(table).get_all(data)

    def save_items(self, data, table, conflict="update"):
        """Save items to specified tables"""
        return rdb.table(table)\
                .insert(data, conflict=conflict)\
                .run()

    def set_last_access(self, event):
        """Save last access time for specified event"""
        data = {
            "id": event,
            "last_access": datetime.now()
        }

        return rdb.table("settings")\
                  .insert(data, conflict="update")\
                  .run()

    def get_last_access(self, event):
        """Get last access time for specified event"""
        return rdb.table("settings").get(event).run()

