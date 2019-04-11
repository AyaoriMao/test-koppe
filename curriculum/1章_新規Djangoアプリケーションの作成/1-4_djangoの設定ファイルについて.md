# djangoプロジェクトの設定ファイルについて

このパートではdjangoプロジェクトを作成すると自動生成される設定ファイル(settings.py)について少し解説します。

## 修正する設定項目

* INSTALLED_APPS
    * そのプロジェクト内に組み込みたいアプリを列挙します。デフォルトでは以下のアプリがすでに組み込まれております。前パートでマイグレーションをした際にはここに記載されているアプリ内のマイグレーションファイル達が実行されていました。自分でアプリを作成した際には、そのアプリをプロジェクトに認識させるため、この設定項目に追加する必要があります。具体的な記載方法ですが以下の２パターンあります。
        * アプリ作成時に自動生成されたapps.pyに定義されているConfigクラスまでのパスを指定する(今回のケースでいうと"amazon.apps.AmazonConfig")
        * プロジェクトのルートフォルダからアプリフォルダのパス(今回でいうと"amazon"にあたります)を指定する
    

    ``` 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ```

    では実際にamazonアプリをこのプロジェクトに追加しましょう。今回はConfigファイルを指定する方法を採用します。
    ではこの項目を以下のように修正します。
    ``` 
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'amazon.apps.AmazonConfig' # 追加
    ]
    ```
* TEMPLATES
    * 利用するテンプレートエンジン(Backend)やテンプレートファイルを格納するディレクトリを指定します。今回、テンプレートファイルはプロジェクトルートフォルダに新しくtemplatesフォルダを作成しましょう。
    ```
    techpit/
    　 ├ manage.py
    　 ├ templates # 新規作成
    　 └ techpit/
        ├ __init__.py
        ├ __pycache__/
        ├ settings.py
        ├ urls.py
        └ wsgi.py
    ```
    フォルダを作成したら設定を当項目のDIRS部分を修正しましょう。
    ```
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')], # 今追加したディレクトリを追加
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

* LANGUAGE_CODE、TIME_ZONE
     * 言語、タイムゾーンを指定します。以下のように修正します。
     ```
     LANGUAGE_CODE = 'ja'
     TIME_ZONE = 'Asia/Tokyo'
     ```

* MEDIA_ROOT、MEDIA_URL
    * MEDIA_???という設定項目は基本的にユーザからアップロードされたファイルやDjangoアプリ内で生成したファイルが格納される場所を定義する項目になります。MEDIA_ROOTは、ファイルが、アップロードやプログラムを通じてDjango内に取り込まれる際のルートフォルダを指定します。MEDIA_URLはMEDIA_ROOTへのアクセスさせるURLを指定します。例をあげると、例えばMEDIA_ROOTを"プロジェクトルート/media"といフォルダにした上で、ユーザからの画像アップロードを受け付けるよう機能を作成したとすると、そのアップロードされた画像ファイルは"プロジェクトルート/media"配下に保存されます。また合わせてMEDIA_URLを"/mymedia/" と設定していたとすると、例えばそのアップロードしたファイルに外部からアクセスさせようとすると、/mymedia/ファイル名のようにアクセスできるようになります。まとめるとMEDIA_ROOTはそのプロジェクト内に取り込んだファイルを保管する場所を指定し、MEDIA_URLはそのMEDIA_ROOTを外部にどのようなURLで公開するのかを定義します。
    では今回はプロジェクトルートの下にmediaフォルダを作成し、そのフォルダをMEDIA_ROOTとすることにします。MEDIA_URLは/media_techpit/としておきましょう。

```
techpit/
　     ├ amazon/ 
　 ├ manage.py
　 ├ templates/ 
　 ├ media # 新規作成
　 └ techpit/
    ├ __init__.py
    ├ __pycache__/
    ├ settings.py
    ├ urls.py
    └ wsgi.py
```

    ```
    MEDIA_ROOT = os.path.join(BASE_DIR,'media') # 追加
    MEDIA_URL = '/media_techpit/' # 追加  
    ```

* STATIC_ROOT
    * こちらは本番環境(django開発サーバではなく、apache, gunicorn等)のWebサーバに静的ファイルを管理させる場合に設定が必要になります。開発用サーバを用いて動かしている段階では、djangoが勝手に各アプリフォルダ直下のstaticフォルダを自動で探してくれるため、意識する必要はないのですが、先述のWebサーバにそれらの静的ファイルを管理させる場合、それらのファイルを一箇所に集めることが必要になり、その”どこに集めるのか”を決めるのがこの設定値になります。具体的には、python manage.py collectstatic　コマンドを打った際に各アプリの静的ファイルを集約する先を指定します。


* STATIC_URL
    * こちらの設定値は、静的ファイルをどんなURLで公開するのかを決めます。例えば、”/static/”とした場合、このプロジェクトにおいて、各静的ファイルは"ドメイン/static/????"のような形でアクセスできるようになります。こちらは特に物理的なフォルダとの紐付けはないため、特にこだわりがなければ、デフォルトで記載されている"/static/"として問題ないでしょう。

* STATIC_DIRS
    * 開発サーバで動かしている段階では、勝手にアプリフォルダのstaticフォルダ内を精査してくれますが、もしそれ以外に静的ファイルフォルダとして認識してほしいフォルダがあれば記載します。基本的には必要ないでしょう。

上記踏まえ、方針を静的ファイルの保持の方針を以下のようにしましょう。
* アプリで利用する静的ファイルはアプリフォルダにstaticフォルダを作成し、そこに格納する。STATIC_DIRSは設定しない
* STATIC_URLは”/static/”とする
* STATIC_ROOTはプロジェクトルート直下のstaticフォルダとする(いじらない)

この場合、設定値は以下のようになります。

```
techpit/
　 ├ amazon/
　   ├ static/ # 新規作成
　 ├ manage.py
　 ├ templates/ 
　 ├ media 
　 └ techpit/
    ├ __init__.py
    ├ __pycache__/
    ├ settings.py
    ├ urls.py
    └ wsgi.py
```
```
STATIC_ROOT = os.path.join(BASE_DIR,'static') # 追加
STATIC_URL = '/static/' # そのまま
```

STATIC_ROOTに指定したフォルダが存在しませんが、
本番で動かす際にcollectstaticコマンドを実行することで、自動的に作成されるため不要です。
とりあえず現段階では以上の修正のみとして次に進みましょう。

## djangoプロジェクトの開発の流れについて
ここまででプロジェクト全体に関わる環境構築や設定値にについて触れました。
ここからは実際にアプリの作成に移りますが、その前にどのような流れで開発を進めてくのかざっくりと把握しておきましょう。どのファイルから記述していくかは人それぞれですが、今回は各ページ以下のステップに則って作成していくこととしましょう。

* STEP 1 モデルの定義
    * djangoでは、そのアプリで利用するデータをモデルとして定義します。モデルはアプリフォルダの下に生成されているmodels.pyに、django.db.models.Modelのサブクラスとして定義します。ここで定義したモデルは、マイグレーション時にデータベースに反映されます(そのモデルの内容のテーブルが自動生成されます)。

* STEP 2 フォームの作成
    * フォームは、htmlのformとdjango内のオブジェクトの仲立ちをし、formの入力値からオブジェクトを作成したり、逆に定義したフィールドに即したformの自動生成といった機能を提供します。フォームはdjango.forms.Formやdjango.forms.ModelFormを継承して作成します。特に後者のModelFormは非常に強力な機能で、各モデルに対するCRUD操作を非常に簡単に実装できるようになります。

* STEP 3 テンプレートの作成
    * テンプレートとは、Webページの「雛形」を定義するファイルになります。テンプレートは基本的には普通のhtmlファイルと同じように記述しますが、中にアプリケーション内で定義した変数にアクセスしたり、if文やfor文を用いて動的にHTMLソースコードを作成できる仕組みが有ります。

* STEP 4 ビューの作成
    * ビューとは、Djangoアプリ内でリクエストを処理する部分になり、リクエストオブジェクトを引数にレスポンスを返す関数になります。クラスベースビューとは上記で記載したレスポンスを返す関数を持つクラスのことを指し、djangoでは汎用クラスベースビューとして、シチュエーション毎に利用できる便利なクラスが用意されており、今回は基本的に、これらの既に用意されている汎用ビューを継承してビューを構築することにします。

* STEP 5 ルーティングの修正
    * ルーティングとは、URLに対して処理(ビュー)を紐づけることを指し、プロジェクトフォルダに生成されているurls.pyに記載します。いくらビューを作成しても、URLに対して作成したビューを紐づけない限りdjangoはそのビューを利用してくれません。

では次章から実際に各Webページを作成していきましょう。