from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><head></head><body><p>Hello World!</p></body></html>"
    
