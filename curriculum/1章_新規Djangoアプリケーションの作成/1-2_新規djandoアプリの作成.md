# 新規Djnagoアプリの作成

## 新規djangoアプリの作成
プロジェクトの作成が完了したので、次にdjangoアプリを作成していきましょう。
ここではmanage.pyが提供するアプリの雛形作成コマンドを利用します。
今回は”amazonm”というアプリを"techpit"プロジェクトに追加しましょう。

```
(myenv)$ python manage.py startapp amazon
(myenv)$ ls
amazon db.sqlite3 manage.py techpit
```
コマンド完了後にフォルダ内をみてみると、amazonフォルダとdb.sqlite3ファイルが新しくできていると思います。amazonフォルダの中身は以下のようになっております。db.sqlite3はデフォルトでdjangoが利用するデータベースファイルになります。

```
amazon/
　├ __init__.py
　├ apps.py
　├ models.py
　├ views.py
　├ admin.py
　├ migrations/
　└ test.py
```
よく修正するファイルとその役割は以下の通りです。
* models.py : データ（テーブル）の定義をします
* views.py : リクエストを処理する関数、およびクラスを定義します
* admin.py : Django管理画面の定義を行います。

以上で今回のパートは終了です。

お疲れ様でした。