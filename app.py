# @app.route('/', methods=['GET','POST'])
# def my_form_post() -> 'html':


from flask import Flask, render_template, request
import subprocess as s
import time, os


app = Flask(__name__)

file1 = open('cach.txt', 'r')
# print(file.read())
f = file1.read()


@app.route('/')
def appp():
    return 'duh  '+str(f)

if __name__=="__main__":
    app.run(debug=True)
