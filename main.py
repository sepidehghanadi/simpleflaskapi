from flask import *
import json
import time


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    ds = {'Page': 'Home', 'Message': 'succesfully loaded!',
          'Timestamp': time.time()}
    json_dump = json.dumps(ds)
    return json_dump


@app.route('/user/', methods=['GET'])
def req_page():
    user_query = str(request.args.get('user'))
    ds = {'Page': 'Request', 'Message': 'succesfully got the request for {user_query}',
          'Timestamp': time.time()}
    json_dump = json.dumps(ds)
    return json_dump


if __name__ == '__main__':
    app.run(port=7776)
