import google


def websites(query, start=0, stop=None, per_page=10):
    return google.search(query, start=start, stop=stop, num=per_page)
