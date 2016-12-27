from .. import md
from . import main
from flask import render_template,request,flash
from .util import TPB,get_tags,time_format,get_archive
from ..config import POST_PATH
import os,re


@main.route("/archive/<time>")
def archive(time):
    index = POST_PATH+"info.md"
    year,month = time.split("-")
    with open(index,'r',encoding='utf-8') as f:
        text = f.read()
        posts = re.findall("\*\s{1}\[([\u4E00-\u9FA5\-\w \&\/\、\(\)]+)\]\(([\w\d_ \.\-]+)\)(#[\w\u4E00-\u9FA5\s,]+#)*",text)
        i = [ post for post in posts]
        posts=[]
        for name,url,tags in i:
            gitlog = os.popen("cd {0} ; git log {1}".format(POST_PATH,url)).read()
            x = re.findall("Date:([\w\d :+]+)\+",gitlog)
            sub_time = time_format(x[-1])
            y, m, d = sub_time.split("-")
            if year != y and month != m:
                file = POST_PATH + url
                with open(file,"r") as f:
                    summary = f.read().split("<!-- more -->")[0]
                    summary = md.convert(summary)
                posts.append((name,url,tags,sub_time,summary))
    return render_template("posts_by_archive.html", posts=posts[::-1], tags=get_tags(),archive=get_archive())
@main.route("/tags/<tag>")
def tags(tag):
    index = POST_PATH+"info.md"
    with open(index,'r',encoding='utf-8') as f:
        text = f.read()
        posts = re.findall("\*\s{1}\[([\u4E00-\u9FA5\-\w \&\/\、\(\)]+)\]\(([\w\d_ \.\-]+)\)(#[\w\u4E00-\u9FA5\s,]+#)*",text)
        i = [ post for post in posts if tag in post[2]]
        posts=[]
        for name,url,tags in i:
            #得到tags
            tags = tags[1:-1].split(",")
            tags = [tag+str(hash(tag)%6+1) for tag in tags]
            #
            gitlog = os.popen("cd {0} ; git log {1}".format(POST_PATH,url)).read()
            x = re.findall("Date:([\w\d :+]+)\+",gitlog)
            sub_time = time_format(x[-1])
            file = POST_PATH + url
            with open(file,"r") as f:
                summary = f.read().split("<!-- more -->")[0]
                summary = md.convert(summary)
            posts.append((name,url,tags,sub_time,summary))
    return render_template("posts_by_tag.html",posts=posts[::-1],tags=get_tags(),archive=get_archive())

@main.route("/p_v2/<name>")
def post_v2(name):
    file  = POST_PATH+name+".md"
    with open(file,'r',encoding='utf-8') as f:
        content = md.convert(f.read())
    gitlog = os.popen("cd {0} ; git log {1}.md".format(POST_PATH,name)).read()
    x = re.findall("Date:([\w\d :+]+)\+",gitlog)
    sub_time = time_format(x[-1])
    up_time = time_format(x[0])
    if sub_time==up_time:
        up_time = False
    return render_template("p_v3.html",content=content,title=name,sub_time=sub_time,up_time=up_time,tags = get_tags(),archive=get_archive())

@main.route("/")
def post_by_summary():
    index = POST_PATH+"info.md"
    with open(index,'r',encoding='utf-8') as f:
        text = f.read()
        i = re.findall("\*\s{1}\[([\u4E00-\u9FA5\-\w \&\/\、\(\)]+)\]\(([\w\d_ \.\-]+)\)(#[\w\u4E00-\u9FA5\s,]+#)*",text)
        posts=[]
        for name,url,tags in i:
            gitlog = os.popen("cd {0}; git log {1}".format(POST_PATH,url)).read()
            x = re.findall("Date:([\w\d :+]+)\+",gitlog)
            sub_time = time_format(x[-1])
            tags = tags[1:-1].split(",")
            tags = [tag+str(hash(tag)%6+1) for tag in tags]

            file = POST_PATH + url
            with open(file,"r") as f:
                summary = f.read().split("<!-- more -->")[0]
                summary = md.convert(summary)
            posts.append((name,url,tags,sub_time,summary))
    all_tags = get_tags()
    archive = get_archive()
    return render_template("index.html",posts=posts[::-1],tags=all_tags,archive=archive)


@main.route("/book_hook",methods=['POST'])
def bookhook():
    '''
    this hook is used to update blog posts
    '''
    if request.method=='POST' :
        os.system("cd {0} ; git pull".format(POST_PATH))
    return "ok"


@main.route('/hook',methods=['POST'])
def hook():
    '''
    this hook is used to update blog program
    '''
    os.system("cd /root/gine ; git pull ")
    os.popen(" pkill gunicorn && gunicorn manage:app")
    return "ok"

@main.route("/meiju",methods=['POST','GET'])
def meiju():
    if request.method== "POST":
        name = request.form['name']
        added = request.form['added']
        res,flag = TPB(name,added).get_magnet_info()
        if flag:
            res= res[:10]
        return render_template("meiju.html",res=res,flag=flag)
    else:
        return render_template("meiju_kong.html")
@main.route("/test")
def testnew():
    return "ok"