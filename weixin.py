from flask import Flask
from flask import request
from flask import  make_response
import hashlib
import traceback
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def weixin_auth():
    try:
        if request.method == 'GET':
            token = 'toto996'
            data = request.args
            signature = data.get('signature', '')
            timestamp = data.get('timestamp', '')
            nonce = data.get('nonce', '')
            echostr = data.get('echostr', '')
            s = [timestamp ,nonce, token]
            s.sort()
            s = ''.join(s)
            if (hashlib.sha1(s).hexdigest() == signature):
                return make_response(echostr)
            return make_response("get ok")
        elif request.method == 'POST':
            return make_response("post ok")
    except Exception, exp:
        print(traceback.format_exc())

if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port = 80)
    except Exception, exp:
        print(traceback.format_exc())
