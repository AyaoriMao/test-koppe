# 開発を進める上で必要なツール（win）
このパートでは開発を進める上で必要なツールを紹介します。ここで紹介しているツールはあくまで私のおすすめなツールなので、ご自身で慣れているツール等を既にお使いであればこのパートは読み飛ばしても構いません。初めてテキストエディタやターミナルを使う方は是非参考にしてください。

**※）今回のパートはPCがwinの方を対象としています。**

**※）既にお手元のwinにエディタがある方はこちらのパートを読み飛ばして構いません。**

## python 3.7のインストール
最新のpythonをインストールしましょう
[![Image from Gyazo](https://i.gyazo.com/4ed2914ca122129edd68d3710527b896.png)](https://gyazo.com/4ed2914ca122129edd68d3710527b896)

下にスクロールするとダウンロードできるバージョンのリストがありますので、python3.7.3を選択しましょう。


python 3.7.3のページに移動した後、下にスクロールするとプロセッサ毎のインストーラが列挙されておりますので、ご自身のPCに合ったインストーラをダウンロードしましょう。ウェブベースや実行可能(exe)ファイル等選択肢がありますが、今回は64bit(Windows x86-64 executable installer)をダウンロードします。
** 64bit PCの方は32bitのpythonを動かせますが、32bit PCの方は32bit python 出ないと動かせないのでご注意ください。

[![Image from Gyazo](https://i.gyazo.com/1f92c8ee4e71a0b04d1e04e689be1c4e.png)](https://gyazo.com/1f92c8ee4e71a0b04d1e04e689be1c4e)


ダウンロードしたインストーラを実行します。
[![Image from Gyazo](https://i.gyazo.com/7f5af9b4aad7bc7afbba229f871693eb.png)](https://gyazo.com/7f5af9b4aad7bc7afbba229f871693eb)

正しくインストールされました。
[![Image from Gyazo](https://i.gyazo.com/6d0ba6c506498c95cb584e621063d9bc.png)](https://gyazo.com/6d0ba6c506498c95cb584e621063d9bc)

試しにコマンドプロンプトで以下のコマンドを打ってみましょう
```
> python --version
Python 3.7.3 
```
上記のようにバージョンが表示されたらうまくインストールできております。

## python 仮想環境の構築
python3.7の仮想環境を構築していきます。仮想環境とは、同じPC上で複数のpythonバージョンを使い分けたり、プロジェクト毎に環境を構成するために仕組みであり、python3.xでは組み込みでそのコマンドが用意されております。まずはプロジェクトを構築するフォルダに移動して、以下のコマンドを打ってください。今回は"myenv"という名前の仮想環境を作成することにします。
```
> python -m venv myenv
> dir
myenv
```
どうフォルダにmyenvというフォルダが作成されております。このmyenvフォルダこそが仮想環境であり、pythonのバージョン(今回で言うと3.7.3)や、これからインストールするパッケージが保管されます。次に、仮想環境に”入って”みましょう。
仮想環境に入るには同じフォルダへ以下のコマンドを打ちましょう。
```
> myenv\Script\activate
(myenv)>
```
すると先頭に仮想環境の名前が表示されます。これで仮想環境に入れました。
この状態で先ほどのコマンドをもう一度打ってみましょう。


仮想環境から出る場合は以下のコマンドを打ちましょう。
```
(myenv)> deactivate
>
```
先頭の(myenv)が無くなりました。これで仮想環境から出たことになります。

これでpython環境の構築は完了です。以降は1章で再開します。

## テキストエディタ
プログラミングをしていく上で必要であるテキストエディタを準備します。

テキストエディタとは、テキストファイルを作成・編集・保存するためのソフトウェアです。


## Visual Studio Code
本講座ではVisual Studio CodeというMicrosoftが開発したオープンソースのテキストエディタの導入方法を説明していきます。Visual Studio Codeは通称VSCodeと呼ばれ、無料で利用できます。


## Visual Studio Codeの導入方法
ではVisual Studio Codeのインストール方法を説明していきます。

まず以下のリンクからVisual Studio Codeをダウンロードしてください。

[Visual Studio Codeのダウンロードページ](https://code.visualstudio.com/)

[![Image from Gyazo](https://i.gyazo.com/1c7c9d22aa4c8a78b42b2619a46b0434.png)](https://gyazo.com/1c7c9d22aa4c8a78b42b2619a46b0434)



インストールウィザードに従いインストールします。
[![Image from Gyazo](https://i.gyazo.com/6c5aa339d6dab399f28d6c2f72a63777.png)](https://gyazo.com/6c5aa339d6dab399f28d6c2f72a63777)

インストールが完了しました。
[![Image from Gyazo](https://i.gyazo.com/855df5df17270b9c83ad5da86218c376.png)](https://gyazo.com/855df5df17270b9c83ad5da86218c376)

拡張機能をインストールします。
下記の画像のように左側にあるアイコンをクリックしてください。

![image](https://i.gyazo.com/b632f955a063c851c4b76315c2e13e4c.png)


すると拡張機能のMARKETPLACEが表示されるので、検索バーからインストールしたい拡張機能を検索しましょう。

![image](https://i.gyazo.com/182e29f848be2617b979606d4ae0dcd5.png)


ここでは最低限としてPythonと日本語化パックをインストールしましょう。(それぞれ"Python", "Japanese"と検索すると一番上に出てくると思います。)
[![Image from Gyazo](https://i.gyazo.com/fccfb6311a4c5ffd7773f78a7db0a518.png)](https://gyazo.com/fccfb6311a4c5ffd7773f78a7db0a518)

[![Image from Gyazo](https://i.gyazo.com/12f5f2f1d094795905ebfe6a51c9ce25.png)](https://gyazo.com/12f5f2f1d094795905ebfe6a51c9ce25)

全てインストールできたらVSCodeを**再起動**してください。再起動することで拡張機能が使えるようになります。

## sqlite3のダウンロード
Djangoのプロジェクトではデフォルトでsqlite3をデータベースエンジンとして利用します。今回のプロジェクトもこのsqlite3をデータベースとして利用します。
そのためデータベースの中身を確認するためにコマンドラインツールのインストールが必要になりますのでダウンロードします。
[公式サイト](https://sqlite.org/download.html)のダウンロードページで、Precompiled Binaries for Windowのsqlite-tools-win32-x86-3270200.zipをダウンロードします。

[![Image from Gyazo](https://i.gyazo.com/5dd2da951151fe771a15b939342ac0c2.png)](https://gyazo.com/5dd2da951151fe771a15b939342ac0c2)

ダウンロードしたzipファイルを任意の場所に解凍してください。後ほど中に入っているsqlite3.exeファイルを利用します。


## コマンドプロンプト
djangoのコマンドを実行するインターフェースとしてコマンドプロンプトを利用します。
コマンドの違いはあれど、基本的にはMacにおけるターミナルと同じように利用できます。

以上で今回のパートは終了です。

お疲れ様でした。