# 新規Djnagoプロジェクトの作成

## Djangoのインストール
この教材の主役であるDjangoをインストールしましょう。
ではまず先ほど作成したmyenv環境に入りましょう。
```
$ source myenv/bin/activate
(myenv)$ 
```

環境に入ったらpipコマンドでdjangoをインストールします。
```
(myenv)$ pip install django
(myenv)$ ・・・
・・・・・・・・
successfully installed ・・・
```
上記のようになれば完了です。
一点注意いただきたいのは、仮想環境に入った状況でパッケージをインストールすると「その環境に」インストールされるということです。
このように、他の環境を汚さないで必要なパッケージをインストールでいるということも仮想環境を利用するメリットになります。

続けて後に必要となるPillowもインストールしておきます。
```
(myenv)$ pip install Pillow
(myenv)$ ・・・
・・・・・・・・
successfully installed ・・・
```
これで準備が整いました。

## 新規djangoプロジェクトの作成
djangoプロジェクトって何？と思う方、多いと思います。djangoプロジェクトとは作成するアプリケーション全体の骨格のことだと理解してよいでしょう。後ほど出てくる”アプリ”と何が違うのかという点ですが、プロジェクトが作成するWebサイト全体を指すのに対し、アプリは何かの機能を実現するためのモジュール群になります。つまり、プロジェクトはその中に複数のアプリを持つことができ、アプリはそのプロジェクトから取り出し、別のプロジェクトに移植することも可能です。
djangoでは、プロジェクトの雛形を自動生成するコマンドを用意してくれているのでそれを利用します。では仮想環境に入った状態で以下のコマンドを打ちましょう。
ここでは新しく"techpit"というプロジェクトを作成します。

```
(myenv)$ django-admin startproject techpit
(myenv)$ ls
techpit myenv
```
するとカレントフォルダにtechpitというフォルダが作成されます。
中身は以下のようになっております。
```
techpit/
　 ├ manage.py
　 └ techpit/
    ├ __init__.py
    ├ __pycache__/
    ├ settings.py
    ├ urls.py
    └ wsgi.py
```
よく利用するファイルは以下の通りです。
* manage.py : 各種コマンドラインユーティリティを定義しております。(基本的に修正は不要)
* settings.py : プロジェクトの各種設定値を定義します
* urls.py : リクエストのルーティングを定義します

次に、プロジェクトフォルダに入り、以下のコマンドでdjango同梱の開発用サーバを立ち上げてみましょう。
```
(myenv)$ cd techpit
(myenv)$ python manage.py runserver
・・・
Starting development server at http://127.0.0.1:8000/
```
上記のようになっていれば成功です。
記載されているURLにアクセスしてみましょう。

[![Image from Gyazo](https://i.gyazo.com/145c3e4db239bc2ce39dbacd70694e7b.png)](https://gyazo.com/145c3e4db239bc2ce39dbacd70694e7b)

上記のような画面が出れば正しくプロジェクトの作成できています。
これで正しい「骨格」ができたので、Ctrl + Cでサーバを停止し、次のパートでは実際にアプリを作成していきましょう。

以上で今回のパートは終了です。

お疲れ様でした。