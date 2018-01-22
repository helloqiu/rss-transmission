# -*- coding: utf-8 -*-

from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class Feed(BaseModel):
    url = CharField()
    save_path = CharField()
