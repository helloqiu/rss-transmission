
rss-transmission
================


.. image:: https://travis-ci.org/helloqiu/rss-transmission.svg?branch=master
   :target: https://travis-ci.org/helloqiu/rss-transmission
   :alt: Build Status


.. image:: https://codecov.io/gh/helloqiu/rss-transmission/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/helloqiu/rss-transmission
   :alt: codecov


Rss for transmission.

UI Preview
==========


.. image:: https://raw.githubusercontent.com/helloqiu/rss-transmission/develop/ui_preview.png
   :target: https://raw.githubusercontent.com/helloqiu/rss-transmission/develop/ui_preview.png
   :alt: preview


Usage
=====

You can simplify create a python file:

.. code-block:: python

   from rssbot.main import Worker
   from rssbot.config import Config

   if __name__ == "__main__":
       config = Config()
       config.config_update(your_config_file_path)
       w = Worker(config)
       w.run()

Then execute this file with python.
If you want to use systemd, here's an service file example:

.. code-block::

   [Unit]
   Description=RSS Transmission.
   After=network.target transmission-daemon.service

   [Service]
   Type=simple
   ExecStart=/bin/python your_path_file_path
   ExecReload=/bin/kill -s HUP $MAINPID

   [Install]
   WantedBy=multi-user.target

Enjoy!

License
=======

GPLv3
