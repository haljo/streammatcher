'''
Updates all feeds from streams.json and writes results to elasticsearch
'''
import json
import feedparser
import httplib2

with open('streams.json') as streams_file:
    streams = json.load(streams_file)


# Fetch -------------------------------------------------------------------

for index, stream in enumerate(streams):
    url = stream['url']
    print(index, ': Parsing', url)
    feed = feedparser.parse(url)
    
    print(feed.channel.title)

    for entry in feed.entries:
        # generate id, push to elastic search
        print(entry.id, entry.title)

        '''
        h = Http()
        >>> data = {"name": "Joe", "comment": "A test comment"}
        >>> resp, content = h.request("http://localhost:9200/feed/entry/", "POST", urlencode(data))

        '''
