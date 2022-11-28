from flask import Flask, render_template, request
# import subprocess
# rep = 0
# globalize(rep)
# rep = 0
# global rep
app = Flask(__name__)
l=[]
def loop():
  a = 0
  while l<=15:
    a+=1
    time.sleep(2)
    l.append(a)

# @app.route('/')#, methods=['GET','POST'])
# def my_form_post():
@app.route('/')
def my_form_post():
  return 'duh'
#   return 'duh!....!'+str(a)+str(l)

def web():    
  app.run(debug=True)


    
# if __name__==__main__:
import threading
# if __name__ == "__main__":
#     x = threading.Thread(target=loop)#, args=(a,))
#    # threads.append(x)
#     x.start()
#     time.sleep(1)
        
  web()

