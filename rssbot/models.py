# -*- coding: utf-8 -*-

import datetime
from peewee import Model, CharField, ForeignKeyField
from playhouse.apsw_ext import APSWDatabase, DateTimeField

db = APSWDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class Feed(BaseModel):
    url = CharField()
    save_path = CharField()
    title = CharField(default='No name')
    create_time = DateTimeField(default=datetime.datetime.now)
    keywords = CharField(default='[]')
    last_check = DateTimeField(default=datetime.datetime.now)
    last_add = DateTimeField(default=datetime.datetime.now)


class Item(BaseModel):
    title = CharField()
    magnet_link = CharField()
    feed = ForeignKeyField(Feed)
    seen_time = DateTimeField(default=datetime.datetime.now)
    publish_time = DateTimeField()
