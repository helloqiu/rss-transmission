# -*- coding: utf-8 -*-

import pytest
import os
from rssbot.config import Config


def test_config():
    config = Config()
    assert config['update_interval'] == 600
    assert config['server'] == {
        "host": "localhost",
        "port": 9091,
        "rpc_path": "/transmission/rpc"
    }
    assert config['work_dir'] == "~/.config/rss-transmission"


def test_config_update():
    config = Config()
    config.config_update(config_path=os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'settings.json'
    ))
    assert config['update_interval'] == 800
    assert config['server'] == {
        "host": "喵喵",
        "port": 1234,
        "rpc_path": "/喵"
    }
    assert config['work_dir'] == "喵喵喵"

    with pytest.raises(RuntimeError):
        config.config_update(config_path="喵喵")
