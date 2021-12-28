# -*- coding: utf-8 -*-
"""
Created on December 24 2021
@author: Giulio Cornelio Grossi, Ph.D.
@email : giulio.cornelio.grossi@gmail.com
"""

import random
from flask import Flask
from flask import render_template
import tree
import json

app = Flask(__name__)

@app.route('/')
def index():
    # route that renders the home page html
    return render_template('index.html')

@app.route('/getdata', methods=['GET'])
def getdata():
    # this is an API that
    # fetches the information to construct the tree
    # of the tree. Wen called with AJAX return a json with the info
    dicttree = tree.get_tree()
    return json.dumps(dicttree,separators=(',', ':'))

@app.route('/light', methods=['GET'])
def light():
    # this is an API that
    # draws a random row of the dataframes representing the lights
    # of the tree. Wen called with AJAX return a json with the info
    dict_light= {}
    i = random.randint(0,len(app.config['xl']))    
    dict_light['x'] = app.config['xl'].loc[i,:].to_list()
    dict_light['y'] = app.config['yl'].loc[i,:].to_list()
    dict_light['size'] = app.config['xs'].loc[i,:].to_list()

    return json.dumps(dict_light,separators=(',', ':'))

if __name__ == '__main__':
    # before running the app we assign the dataframes with the
    # coordinates of the lights as a global app variables
    app.config['xl'],app.config['yl'],app.config['xs'] = tree.get_lights()
    # we run the app
    app.run(host='127.0.0.1', port=8080, debug=True)