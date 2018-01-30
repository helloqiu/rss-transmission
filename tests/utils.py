# -*- coding: utf-8 -*-


class test_database(object):
    def __init__(self, db, models, create_tables=True, drop_tables=True,
                 fail_silently=False):
        if not isinstance(models, (list, tuple, set)):
            raise ValueError('%r must be a list or tuple.' % models)
        self.db = db
        self.models = models
        self.create_tables = create_tables
        self.drop_tables = drop_tables
        self.fail_silently = fail_silently

    def __enter__(self):
        self.orig = []
        for m in self.models:
            self.orig.append(m._meta.database)
            m._meta.database = self.db
        if self.create_tables:
            self.db.create_tables(self.models)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.create_tables and self.drop_tables:
            self.db.drop_tables(self.models)
        for i, m in enumerate(self.models):
            m._meta.database = self.orig[i]
