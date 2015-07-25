from flask import Flask
from flask import request
from flask import  make_response
import hashlib
import traceback
import time
import xml.etree.ElementTree as ET
app = Flask(__name__)

def CDATA(text=None):
    element = ET.Element('![CDATA[')
    element.text = text
    return element

@app.route('/fzcb', methods=['GET','POST'])
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
            xmlData = ET.fromstring(request.data)
            # print(request.data)
            toUserName = xmlData.find("ToUserName").text
            fromUserName = xmlData.find("FromUserName").text
            msgType = xmlData.find("MsgType").text
            content = "?"
            if msgType == "text":
                content = xmlData.find("Content").text

            print(toUserName, fromUserName, msgType, content)
            root = ET.Element("xml")
            ET.SubElement(root, "ToUserName").text = fromUserName
            ET.SubElement(root, "FromUserName").text = toUserName
            ET.SubElement(root, "CreateTime").text = str(int(time.time()))
            ET.SubElement(root, "Content").text = content
            ET.SubElement(root, "MsgType").text = "text"
            strReplay = ET.tostring(root, "utf-8").decode("utf-8")
            resp = make_response(strReplay)
            resp.content_type = 'application/xml'
            return resp
            # reply = u"<xml><ToUserName>{}</ToUserName><FromUserName>{}</FromUserName><CreateTime>{}</CreateTime><MsgType><![CDATA[text]]></MsgType><Content>{}</Content></xml>"
            # reply = reply.format(fromUserName, toUserName, str(int(time.time())), content)
            # response = make_response(reply)
            # return response
    except Exception, exp:
        print(traceback.format_exc())

if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port = 80)
    except Exception, exp:
        print(traceback.format_exc())
