# -*- coding: utf-8 -*-

import feedparser
import requests
import datetime
from rssbot.models import Feed


class Feeder(object):
    def add(self, url, save_path):
        Feed.create(url=url, save_path=save_path)
        return True

    def get_all_feeds(self):
        feeds = Feed.select()
        return feeds

    def parse_items(self, content):
        d = feedparser.parse(content)
        result = list()
        for entry in d['entries']:
            item = dict(
                title=entry['title'],
                publish_time=datetime.datetime(*tuple(entry['published_parsed'])[:-2])
            )
            for link in entry['links']:
                if link['type'] == 'application/x-bittorrent':
                    item['magnet_link'] = link['href']
                    break
            result.append(item)
        return result
