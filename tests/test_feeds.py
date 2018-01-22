# -*- coding: utf-8 -*-

import os
from rssbot.feeds import Feeder
from rssbot.models import db, Feed


def setup_module():
    db.init('test.db')
    db.create_tables([Feed])


def teardown_module():
    os.remove('test.db')


def test_feeds_add():
    feeder = Feeder()
    feeder.add(url='喵喵', save_path='喵')
    feeds = feeder.get_all_feeds()
    assert len(feeds) == 1
    assert feeds[0].url == '喵喵'
    assert feeds[0].save_path == '喵'


def test_feed_parse_items():
    feeder = Feeder()
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'example.xml'), 'r') as f:
        content = f.read()
    items = feeder.parse_items(content)
    item = items[0]
    assert item['title'] == 'Item标题'
    assert item['magnet_link'] == 'magnet:?xt=urn:btih:233'
