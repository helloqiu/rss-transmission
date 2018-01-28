# -*- coding: utf-8 -*-

import json
from flask import Flask, request, jsonify, make_response, render_template
from playhouse.shortcuts import model_to_dict
from rssbot.models import Feed, Item

app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route('/api/feeds', methods=['GET', 'POST', 'DELETE'])
def feeds():
    if request.method == 'GET':
        all_feeds = Feed.select()
        result = list()
        for feed in all_feeds:
            temp = model_to_dict(feed)
            temp['create_time'] = temp['create_time'].strftime('%Y-%m-%d %H:%M')
            temp['last_check'] = temp['last_check'].strftime('%Y-%m-%d %H:%M')
            temp['last_add'] = temp['last_add'].strftime('%Y-%m-%d %H:%M')
            temp['keywords'] = json.loads(temp['keywords']) if temp['keywords'] else []
            result.append(temp)
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
        temp = model_to_dict(item)
        temp['seen_time'] = temp['seen_time'].strftime('%Y-%m-%d %H:%M')
        temp['publish_time'] = temp['publish_time'].strftime('%Y-%m-%d %H:%M')
        result.append(temp)
    return jsonify(result)


@app.route('/')
def index():
    return render_template('index.html')
