# ここに画像検索のAPIを叩く処理を書いてね
import requests
import json
from os import chdir,getcwd
from os.path import dirname

if __name__ == "__main__":
    chdir(dirname(__file__))
    print(getcwd())

with open("UnsplashAPIkey.json") as f:
    KEYS = json.load(f)
    
def image(flower_name):
    print(flower_name)
    return "https://picsum.photos/200/300"#例示を画像URLに変更

if __name__ == "__main__":
    print(KEYS)