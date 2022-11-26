from flask import Flask, render_template, request
# import subprocess
# rep = 0
# globalize(rep)
# rep = 0
# global rep
app = Flask(__name__)


# @app.route('/')#, methods=['GET','POST'])
# def my_form_post():
@app.route('/')
def my_form_post():
  return 'duh!....!'

# if __name__==__main__:
app.run(debug=True)
