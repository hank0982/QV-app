import json
import json.decoder
import os
import random
import uuid
from pprint import pprint
from sys import exit

import requests
from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from datetime import datetime
from server import app, db
from server.utils import decide_path

@app.route('/')
def root():
    return jsonify({"string":"welcome"})
	#return app.send_static_file('index.html')

@app.route('/createUser', methods=['POST'])
def welcome():
	""" Once the user decides to move on, create a user and nsave to database.
	return database object id as user id, flow.
	"""

	user = {
		"userid": "",
		"create_time": datetime.utcnow(),
		"complete_flag": False
	}

	userid = db.user.insert_one(user).inserted_id

	# update user path
	user["path"] = decide_path()
	user["userid"] = userid

	db.user.update_one({
	  '_id': userid
	},{
	'$set': user
	}, upsert=False)

	return jsonify(user), 200


@app.route('/submit', methods=['POST'])
def submit():
	print(request.json)
	insert_data = {
		"form": "qv598"
	}
	db.test.insert_one(insert_data)
	return jsonify({'ok': True}), 200

@app.route('/qv/<string:file_name>')
def show_subpath(file_name):
    file_name = '/'.join(['data', file_name])
    filename = os.path.join(app.static_folder, file_name+'.json')
    # data is a json file
    data = json.load(open(filename))
    return jsonify(data)
