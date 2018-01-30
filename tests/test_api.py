# -*- coding: utf-8 -*-

import json
import copy
from rssbot.web import app as application
from rssbot.models import Feed
from playhouse.test_utils import test_database
from playhouse.sqlite_ext import SqliteExtDatabase
from playhouse.shortcuts import model_to_dict
from webtest import TestApp as Application

temp_db = SqliteExtDatabase(":memory:")
feed_data = dict(
    url='http://喵喵喵.test',
    save_path='/233/喵喵',
    title='喵'
)


def test_feed_get():
    app = Application(application)
    with test_database(temp_db, (Feed,)):
        Feed.create(**feed_data)
        resp = app.get('/api/feeds')
        resp = json.loads(resp.body.decode('utf-8'))
        assert len(resp) == 1
        resp = resp[0]
        for k in feed_data.keys():
            assert feed_data[k] == resp[k]


def test_feed_post():
    app = Application(application)
    with test_database(temp_db, (Feed,)):
        # create
        resp = app.post('/api/feeds', json.dumps(feed_data), content_type='application/json')
        assert resp.status == '200 OK'
        resp = resp.body.decode('utf-8')
        assert resp == 'OK'
        all_feeds = list(Feed.select())
        assert len(all_feeds) == 1
        feed = model_to_dict(all_feeds[0])
        for k in feed_data.keys():
            assert feed_data[k] == feed[k]

        # update
        feed.pop('create_time')
        feed.pop('last_check')
        feed.pop('last_add')
        feed['title'] = '汪'
        resp = app.post('/api/feeds', json.dumps(feed), content_type='application/json')
        assert resp.status == '200 OK'
        resp = resp.body.decode('utf-8')
        assert resp == 'OK'
        all_feeds = list(Feed.select())
        assert len(all_feeds) == 1
        result = model_to_dict(all_feeds[0])
        for k in feed.keys():
            assert feed[k] == result[k]
