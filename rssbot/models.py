# -*- coding: utf-8 -*-

import datetime
from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, DateTimeField

db = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class Feed(BaseModel):
    url = CharField()
    save_path = CharField()


class Item(BaseModel):
    title = CharField()
    magnet_link = CharField()
    feed = ForeignKeyField(Feed)
    seen_time = DateTimeField(default=datetime.datetime.now)
    publish_time = DateTimeField()
