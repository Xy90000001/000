# @app.route('/', methods=['GET','POST'])
# def my_form_post() -> 'html':


from flask import Flask, render_template, request
import subprocess as s
import flask
import time, os

file = open('cach.txt', 'r')
# print(file.read())
f = file.read()

app = Flask(__name__)

@app.route('/')
def index():
    return 'duh'+str(f)

app.run()
