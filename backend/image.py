# ここに画像検索のAPIを叩く処理を書いてね
#ライブラリのインポート
from requests import get,Response
from json import load,loads
from os import chdir,getcwd
from os.path import dirname
from datetime import datetime

#定数の設定
HOWMANY = 1
ASPECTRATE = "4:3" #横:縦
API = "google"#unsplash/google
#Jsonの読み込み
if __name__ == "__main__":
    chdir(dirname(__file__))
    print(getcwd())
with open("APIkey.json") as f:
    KEYS = load(f)


#get処理を分離
def query(url:str,headers,params):
    result = get(url,headers=headers,params=params)
    if result.status_code != 200:
        print(result.status_code)
        print(result.reason)
        return result,1
    return result,0


#アカウントの取得がうまくできず断念.
"""
#画像検索APIにBing Image Searchを用いる場合

def bing(flower_name):
    try:
        result,status = query("https://api.cognitive.microsoft.com/bing/v7.0/images/search",
                    {"Ocp-Apim-Subscription-Key":KEYS["Bing Search API"]["SubscriptionKey"]},
                    {
                    "license":"public",
                    "q":f"(flower|花) {flower_name}",
                    "imageType":"photo",
                    "count":HOWMANY,
                    "aspect":"All"
                    }
                    )
    #https://learn.microsoft.com/ja-jp/bing/search-apis/bing-image-search/reference/query-parameters
    except:
        return 0
    if status == 1:
        return 0
    return result
"""


#画像検索APIにCustom search APIを用いる場合

def google(flower_name):
    #Custom search APIに画像を要求
    try:
        result,status = query("https://customsearch.googleapis.com/customsearch/v1",
                    {},
                    {
                    "key":KEYS['Custom Search API']['APIKey'],
                    "cx":KEYS['Custom Search API']['SearchEngineID'],
                    "q":f"(flower|花) {flower_name}",
                    "fileType":"jpeg png jpg",
                    "searchType":"image",
                    "imgType":"photo",
                    "imgSize":"xlarge",
                    "num":HOWMANY
                    }
                    )
    #https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list?hl=ja
    except:
        return 0
    if status == 1:
        return 0
    
    #抽出返答
    return loads(result.content)["items"][0]["link"]



#画像検索APIにunsplashを用いる場合

#サーバーの起動中保持する変数を設定
last_update = datetime.now().hour
request_is_vailed = True

def unsplash(flower_name):
    """花の写真を指すurlを返します。
    flower_nameは必ず英名の文字列を渡してください。
    何らかのエラーにより画像を取得できなかった場合はintの0を返します。
    """
    global last_update,request_is_vailed

    print(f"get:{flower_name}")
    #クエリを使い果たしたらリクエストを投げない。
    if not request_is_vailed:
        if last_update != datetime.now().hour:
            last_update = datetime.now().hour
        else:
            return 0

    #unsplashAPIに{flower_name}の写真を要求
    try:
        result,status = query("https://api.unsplash.com/photos/random/",
                    {},
                    {
                    "client_id":KEYS['Unsplash']['AccessKey'],
                    "query":flower_name,
                    "count":HOWMANY
                    }
                    )
    except:
        return 0
    if status == 1:
        return 0

    #結果から画像URLを抽出
    parsed_result = loads(result.text)
    raw_image_url = parsed_result[0]["urls"]["raw"]

    #残りクエリ回数を確認
    print("UnsplashAPI: X-Ratelimit-Remaining:",result.headers["X-Ratelimit-Remaining"])
    if result.headers["X-Ratelimit-Remaining"]==0:
        request_is_vailed = False

    #APIの機能を用いて画像を成形
    #refer "https://unsplash.com/documentation#supported-parameters"
    image_url = raw_image_url + f"&ar={ASPECTRATE}&crop=entropy&fit=crop"

    return image_url



def _shift_to_front(list_,element):
    list_.remove(element)
    list_.insert(0,element)

def image(flower_name):
    try_order = [google,unsplash]
    if API=="unsplash":
        _shift_to_front(try_order,unsplash)
    elif API=="google":
        _shift_to_front(try_order,google)
    """
    elif API=="bing":
        return bing(flower_name)
    """

    #複数のAPIを叩けるように処理
    res = 0
    for f in try_order:
        res = f(flower_name)
        if res != 0:
            break
    return res

if __name__ == "__main__":
    print(image("blue rose"))