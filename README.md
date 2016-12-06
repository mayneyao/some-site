##这是什么？
这是一个基于flask和git的简单博客程序，主要有以下几个特性。

+ 利用git以文件形式存储博文。
+ 以gitbook为远程仓库，利用gitbook前端编辑器，实现多终端在线编辑。
+ 使用gitbook的hooks，在线编辑或者本地push之后，博文及时更新。

##功能实现

+ 通过gitbook的SUMMARY.md 实现文章的标签分类。
+ 通过git log追溯文件历史，提取文件发表时间与更新时间。
