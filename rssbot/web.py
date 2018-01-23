# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict
from rssbot.models import Feed

app = Flask(__name__)


@app.route('/api/feeds', methods=['GET', 'POST', 'DELETE'])
def feeds():
    if request.method == 'GET':
        all_feeds = Feed.select()
        result = list()
        for feed in all_feeds:
            result.append(model_to_dict(feed))
        return jsonify(result)
