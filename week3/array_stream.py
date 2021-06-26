def process_array(data):
    return [int(n.decode("utf-8")) for n in data.split(b'\n') if len(n) > 0]