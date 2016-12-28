##这是什么？
这是一个基于flask和git的简单博客程序，主要有以下几个特性。

+ 利用git以文件形式存储博文。
+ 以gitbook为远程仓库，可以利用gitbook前端编辑器。
+ 使用gitbook的hooks，在线编辑或者本地push之后，博文及时更新。

## 实现
+ 在gitbook仓库内，建立info.md(SUMMARY.md+tag信息，这个是手动维护的。)
+ 每次gitbook仓库内容有变动——》hook传递给服务器，服务器更新博文内容。
+ 通过info.md提取出tag分类信息。
+ 通过gitlog 某个博文文件，提取出发表时间和更新时间。
+ 通过gitlog提取的时间进行博文归档。
+ 评论采用第三方评论框（多说）。

## 使用
+ 克隆程序 git clone https://github.com/MayneYao/gine.git
+ 克隆你在gitbook上创建的博文仓库 git clone https://git.gitbook.com/yourgitbook/yourbook.git
+ 安装依赖 
虚拟环境
```
pip install virtualenv
virtualenv -p /usr/bin/python3 venv
```


依赖包
```
beautifulsoup4==4.5.1
Flask==0.11.1
Flask-Script==2.0.5
gunicorn==19.6.0
html5lib==0.999999999
Jinja2==2.8
Markdown==2.6.7
Pygments==2.1.3
requests==2.12.1
Werkzeug==0.11.11
``` 

