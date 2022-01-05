import urllib.request
import urllib.parse
import json
import string

access_token = "输入你的token"  # 输入你的token

def getTranslateResponce(url, data):

    url = urllib.parse.quote(url, safe=string.printable)
    url = url.replace("\n", "%0A")
    url = url.replace(" ", "%20")
    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')

def trans(content):
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + access_token + "&from=auto&to=en&q=" + content
    data = {}
    data['from'] = 'en'  # 源语言语言自动检测
    data['to'] = 'zh'  # 目标语言
    data['q'] = content
    html = getTranslateResponce(url, data)
    target = json.loads(html)
    try:
        return target['result']['trans_result']
    except:
        print(target)
