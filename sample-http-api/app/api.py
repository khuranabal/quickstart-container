from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def home():
    host = str(request.host)
    return Response(host, content_type='text/plain')
