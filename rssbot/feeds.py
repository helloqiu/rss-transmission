# -*- coding: utf-8 -*-

from rssbot.models import Feed


class Feeder(object):
    def add(self, url, save_path):
        Feed.create(url=url, save_path=save_path)
        return True

    def get_all_feeds(self):
        feeds = Feed.select()
        return feeds
