import io, logging
log = logging.getLogger('test')
handler = logging.StreamHandler(io.StringIO())
handler.setFormatter(logging.Formatter('%(msg)s'))
log.addHandler(handler)
log.setLevel(logging.INFO)
for msg in ['a', 'b', 'c']:
    log.info(msg)  # calls handler.stream.write
print(handler.stream.getvalue())
