# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, make_response
from playhouse.shortcuts import model_to_dict
from rssbot.models import Feed, Item

app = Flask(__name__)


@app.route('/api/feeds', methods=['GET', 'POST', 'DELETE'])
def feeds():
    if request.method == 'GET':
        all_feeds = Feed.select()
        result = list()
        for feed in all_feeds:
            result.append(model_to_dict(feed))
        return jsonify(result)

    if request.method == 'POST':
        posted_feed = request.get_json()
        if 'id' in posted_feed.keys():
            query = Feed.update(**posted_feed).where(Feed.id == posted_feed['id'])
            query.execute()
        else:
            Feed.create(**posted_feed)
        return make_response('OK', 200)

    if request.method == 'DELETE':
        posted_feed = request.get_json()
        if 'id' in posted_feed.keys():
            query = Feed.delete().where(Feed.id == posted_feed['id'])
            query.execute()
            return make_response('OK', 200)


@app.route('/api/items', methods=['GET'])
def items():
    all_items = Item.select()
    result = list()
    for item in all_items:
        result.append(model_to_dict(item))
    return jsonify(result)