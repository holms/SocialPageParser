import events

e = events.fb_event_collect(
    page_id='theswingcatslt',
    rdb_host = 'rethinkdb',
    rdb_db = 'socialpageparser',
    rdb_table = 'events'
)
e.get_events()
