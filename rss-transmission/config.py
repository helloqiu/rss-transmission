# -*- coding: utf-8 -*-

import os
import json


class Config(dict):
    def __init__(self):
        super(Config, self).__init__()
        self['update_interval'] = 600
        self['server'] = {
            'host': 'localhost',
            'port': 9091,
            'rpc_path': '/transmission/rpc'
        }
        self['work_dir'] = '~/.config/rss-transmission'
        self['feeds'] = list()

    def config_update(self):
        config_path = os.path.join(self['work_dir'], 'settings.json')
        with open(config_path, 'r') as f:
            config = json.loads(f.read())
        for k in config.keys():
            self[k] = config[k]
