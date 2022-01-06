import urllib.request
import urllib.parse
import json
import string

# 此token需要注册百度智能云账号获取,如果嫌麻烦,可以使用免费api方式翻译,就是慢一点
access_token = "输入你的token"  # 输入你的token


def getTranslateResponce(url):

    url = urllib.parse.quote(url, safe=string.printable)
    url = url.replace("\n", "%0A")
    url = url.replace(" ", "%20")
    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')


def transUseMyapi(content):
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + access_token + "&from=auto&to=en&q=" + content
    html = getTranslateResponce(url)
    target = json.loads(html)
    try:
        return target['result']['trans_result']
    except:
        print(target)


def trans(content):
    url = 'https://sp1.baidu.com/5b11fzupBgM18t7jm9iCKT-xh_/sensearch/selecttext?q=' + content
    html = getTranslateResponce(url)
    target = json.loads(html)
    try:
        return target['data']['result']
    except:
        print(target)
        return ''
