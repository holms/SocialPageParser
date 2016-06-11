def jdump(data):
    return json.dumps(data, \
        ensure_ascii=False,
        sort_keys=True,
        indent=2
    )
