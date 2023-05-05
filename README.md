# jackHack2023

## フロントエンドのセットアップ

1. パッケージをインストールする

```
npm install
```

2. ホスティング

```
npm run dev
```

## バックエンドのセットアップ

1. パッケージのインストール

```
pip install -r requirements.txt
```

2. ホスティング

開発環境の場合

```
python3 main.py 
```
本番環境の場合
```
gunicorn main:app
```
