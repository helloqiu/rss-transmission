# -*- coding: utf-8 -*-


import os
from rssbot.config import Config
from rssbot.logger import logger, enable_pretty_logging


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
