# -*- coding: utf-8 -*-


import os
import time
from threading import Thread
import transmissionrpc
from rssbot.config import Config
from rssbot.feeds import Feeder
from rssbot.logger import logger, enable_pretty_logging
from rssbot.models import db, Feed, Item
from rssbot.web import app
from gevent.wsgi import WSGIServer


class Worker(object):
    def __init__(self, config=None):
        self.logger = logger
        enable_pretty_logging(self.logger)
        self.logger.info('Rss transmission start.')
        if config is None:
            self.config = Config()
        else:
            self.config = config
        if not os.path.exists(self.config['work_dir']):
            self.logger.info('Default work dir is not exist.Try to create one.')
            os.makedirs(self.config['work_dir'])
        db.init(os.path.join(self.config['work_dir'], 'rss-transmission.db'))
        Feed.create_table(True)
        Item.create_table(True)
        self.feeder = Feeder()
        self.client = transmissionrpc.Client(
            'http://{}:{}{}'.format(
                self.config['server']['host'],
                self.config['server']['port'],
                self.config['server']['rpc_path']
            )
        )

    def work(self):
        while True:
            try:
                self.logger.debug('Start to update.')
                result = self.feeder.update()
                for item in result:
                    self.logger.info('Get new item:\nTitle: {}\nMagnet: {}'.format(item.title, item.magnet_link))
                    self.logger.debug('\tStart to add torrent to transmission.')
                    self.client.add_torrent(item.magnet_link, download_dir=item.feed.save_path)
                    self.logger.debug('\tAdding done.')
                if len(result) == 0:
                    self.logger.info('Nothing to do.')
                self.logger.info('Update is done.')
                time.sleep(self.config['update_interval'])
            except Exception as e:
                self.logger.info(e)

    def run(self):
        self.logger.info('Rss transmission is running.')
        server = WSGIServer(('0.0.0.0', 9092), app)
        t = Thread(target=self.work)
        t.start()
        server.serve_forever()
