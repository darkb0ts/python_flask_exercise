   
from flask import Flask
app = Flask(__name__)
 
@app.route('/hello/<name>') # add name print your name in website
def hello_name(name):
   return 'Hello %s!' % name
 
if __name__ == '__main__':
   app.run()