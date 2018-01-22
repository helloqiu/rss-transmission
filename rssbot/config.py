# -*- coding: utf-8 -*-

import os
import json


class Config(dict):
    def __init__(self):
        super(Config, self).__init__()
        self.config_update(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'default_settings.json'))

    def config_update(self, config_path=None):
        if not config_path:
            config_path = os.path.join(self['work_dir'], 'settings.json')
        if not os.path.exists(config_path):
            raise RuntimeError('Config path "{}" does not exist!'.format(config_path))
        with open(config_path, 'r') as f:
            config = json.loads(f.read())
        for k in config.keys():
            self[k] = config[k]
