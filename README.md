# rss-transmission

[![Build Status](https://travis-ci.org/helloqiu/rss-transmission.svg?branch=master)](https://travis-ci.org/helloqiu/rss-transmission)
[![codecov](https://codecov.io/gh/helloqiu/rss-transmission/branch/master/graph/badge.svg)](https://codecov.io/gh/helloqiu/rss-transmission)

Rss for transmission.

# UI Preview
[![preview](https://raw.githubusercontent.com/helloqiu/rss-transmission/develop/ui_preview.png)](https://raw.githubusercontent.com/helloqiu/rss-transmission/develop/ui_preview.png)

# Usage
You can simplify create a python file:
``` python
from rssbot.main import Worker
from rssbot.config import Config

if __name__ == "__main__":
    config = Config()
    config.config_update(your_config_file_path)
    w = Worker(config)
    w.run()
```
Then execute this file with python.
If you want to use systemd, here's an service file example:
```
[Unit]
Description=RSS Transmission.
After=network.target transmission-daemon.service

[Service]
Type=simple
ExecStart=/bin/python your_path_file_path
ExecReload=/bin/kill -s HUP $MAINPID

[Install]
WantedBy=multi-user.target
```
Enjoy!

# License
GPLv3
