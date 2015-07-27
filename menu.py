# -*- coding: utf-8 -*-
import urllib2
import urllib
import json

appid = "wx6d84668ba79e8123"
secret = "0c9a2b44f3699c053d54934bc3982192"
url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(appid, secret)
file = urllib2.urlopen(url)
result = json.loads(file.read())
token = result.get("access_token")
print(token)

menuData = {
    "button":[
        {
            'type': 'click',
            'name': u'今日歌曲',
            'key': 'V1001_TODAY_MUSIC'
        },
        {
            'type': 'click',
            'name': u'歌手简介',
            'key': 'V1001_TODAY_SINGER'
        },
        {
            'name': u'菜单',
            'sub_button': [
                {
                    'type': 'view',
                    'name': u'搜索',
                    'url': 'http://www.soso.com/'
                },
                {
                    'type': 'view',
                    'name': u'视频',
                    'url': 'http://v.qq.com/'
                },
                {
                    'type': 'click',
                    'name': u'赞一下我们',
                    'key': 'V1001_GOOD'
                }
            ]
        }
    ]
}

url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={}".format(token)
menuData = json.dumps(menuData, ensure_ascii=False).encode('utf8')
# menuData = urllib.urlencode(menuData)
# menuData = json.dumps(menuData).encode('utf8')

print(menuData)

file = urllib2.urlopen(url, menuData)
result = json.loads(file.read())
print(result)
