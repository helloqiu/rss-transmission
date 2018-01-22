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
