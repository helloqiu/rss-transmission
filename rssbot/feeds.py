# -*- coding: utf-8 -*-

import feedparser
import requests
import datetime
import json
from rssbot.models import Feed, Item


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

    def update(self):
        feeds = self.get_all_feeds()
        result = list()
        for feed in feeds:
            r = requests.get(feed.url)
            items = self.parse_items(r.text)
            for item in items:
                query = Item.select().where(Item.title == item['title'])
                if not query.exists():
                    keywords = json.loads(feed.keywords)
                    new_item = Item(**item, feed=feed)
                    new_item.save()
                    if len(keywords) > 0:
                        for keyword in keywords:
                            if keyword in item['title']:
                                result.append(new_item)
                                Feed.update(last_add=datetime.datetime.now()).where(Feed.id == feed.id).execute()
                                break
                    else:
                        result.append(new_item)
                        Feed.update(last_add=datetime.datetime.now()).where(Feed.id == feed.id).execute()
            Feed.update(last_check=datetime.datetime.now()).where(Feed.id == feed.id).execute()
        return result
