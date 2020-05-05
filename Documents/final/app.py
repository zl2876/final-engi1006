# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""
#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/1006")
def hello():
    return render_template("index3.html")

@app.route("/time")
def paperhouse():
    return render_template("index.html")

@app.route("/thoughts")
def canvas():
    return render_template("index2.html")

#start the server
if __name__ == "__main__":
    app.run()