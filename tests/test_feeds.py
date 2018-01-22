# -*- coding: utf-8 -*-

import os
import responses
from rssbot.feeds import Feeder
from rssbot.models import db, Feed, Item


class TestFeedClass:
    FeedURL = "http://233.com"

    def setup_method(self):
        db.init('test.db')
        db.create_tables([Feed, Item])

    def teardown_method(self):
        os.remove('test.db')

    def test_feeds_add(self):
        feeder = Feeder()
        feeder.add(url='喵喵', save_path='喵')
        feeds = feeder.get_all_feeds()
        assert len(feeds) == 1
        assert feeds[0].url == '喵喵'
        assert feeds[0].save_path == '喵'

    def test_parse_items(self):
        feeder = Feeder()
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'example.xml'), 'r') as f:
            content = f.read()
        items = feeder.parse_items(content)
        item = items[0]
        assert item['title'] == 'Item标题'
        assert item['magnet_link'] == 'magnet:?xt=urn:btih:233'

    @staticmethod
    def feed_callback(request):
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'example.xml'), 'r') as f:
            content = f.read()
        return 200, {'content-type': 'text/xml; charset=utf-8'}, content

    @responses.activate
    def test_update(self):
        responses.add_callback(responses.GET, self.FeedURL, callback=self.feed_callback)

        class FeederForTest(Feeder):
            def send_to_transmission(self, item):
                assert item.title == 'Item标题'
                assert item.magnet_link == 'magnet:?xt=urn:btih:233'

        feeder = FeederForTest()
        feeder.add(url=self.FeedURL, save_path="喵")
        feeder.update()

        items = Item.select()
        item = items[0]
        assert item.title == 'Item标题'
        assert item.magnet_link == 'magnet:?xt=urn:btih:233'
