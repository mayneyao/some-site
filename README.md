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
1. 克隆你在gitbook上创建的博文仓库 
```git clone https://git.gitbook.com/yourgitbook/yourbook.git```
2. 环境&&依赖 
```
pip3 install -r requests.txt
```
3. 配置文件
在app目录下，新建config.py 文件。只需要指定POST_PATH的位置即可，eg:
```
POST_PATH = "/path/to/yourbook/"
```
4. 运行
```
python3 manage.py runserver --host 指定ip，默认本地  --port 指定端口
```



