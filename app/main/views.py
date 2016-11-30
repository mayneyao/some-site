from .. import md,db
from . import main
from flask import render_template,session,flash,redirect,url_for,request
from ..models import Post,User
from .forms import PostForm,LoginForm
from flask.ext.login import login_user,login_required,logout_user
from .util import TPB
import json,os
PER_PAGE=20


@main.route("/tset_hook")
def testhook():
    return "ok2"

@main.route('/manage')
@login_required
def manage():
    all_posts = [(i.title,i.subtime,i.id) for i in Post.query.all()]
    return render_template("manage.html",posts=all_posts)

@main.route('/hook',methods=['POST'])
def hook():
    #request.get_data()
    os.popen("cd /root/gine;git pull;pkill gunicorn && gunicorn manage:app")
    return "ok"

@main.route("/od")
def dulfy():
    if request.method == "POST":
        email = request.form['email']


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


@main.route('/',methods=['POST','GET'])
def index():
    page = request.args.get('page',1,type=int)
    pagination = Post.query.order_by(Post.subtime.desc()).paginate(page,per_page=PER_PAGE,error_out=False)
    posts = pagination.items
    return render_template('allpost.html',posts=posts,pagination=pagination)

@main.route('/p/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    content = post.content
    tag = post.tag.split(",")
    content = md.convert(content)
    return render_template('p.html',post=post,content = content,tag=tag)
    # p_title  = "我的第一篇文章"
    # p_subtime = "2016年7月30日15:42:19"
    # p_times = "2000"
    # with open('E:\\mysite\\templates\\1.md','r',encoding='utf-8') as f:
    #     md = f.read()
    #     p_content = util.md2html(md)
    #
    # post = {'p_title':p_title,'p_subtime':p_subtime,'p_times':p_times,'p_content':p_content,'p_id':p_id}
    # return  render_template('p.html',post=post)

@main.route('/subpost',methods=['POST','GET'])
@login_required
def sub_post():
    # title= None
    # content = None
    # tag = None
    #form = PostForm()
    #if form.validate_on_submit():
    if request.method== 'POST':
        title= request.form["title"]
        tag = request.form["tag"]
        content = request.form["content"]
        #form.title.data=""
        #form.content.data=''
        #form.tag.data=""
        post = Post(title=title,tag=tag,content=content)
        db.session.add(post)
        db.session.commit()
        return  redirect(url_for(".post",id=post.id))

    return render_template('sub_post_v2.html')

@main.route('/edit/<int:id>',methods=['POST','GET'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.title= form.title.data
        post.content= form.content.data
        db.session.add(post)
        db.session.commit()
        flash("文章已经更新")
        return  redirect(url_for('.post',id=post.id))
    form.title.data = post.title
    form.content.data = post.content
    return render_template('edit_post.html',form=form,p_id= post.id)


@main.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(url_for('main.index'))
        flash('账号或密码错误')
    return render_template('login.html',form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you have been logged out.")
    return redirect(url_for('main.index'))

# @main.route('/posts',methods=['POST','GET'])
# def all_post():
#     if request.method =="POST":
#         pass
#     posts = Post.query.all()
#     #posts = posts[-20:-1]
#     posts = reversed(posts)
#     return render_template('allpost.html',posts=posts)

@main.route('/search')
def search():
    pass

@main.route('/test')
def webtest():
    return render_template('logint.html')

@main.route('/wiki/<word>')
def wiki(word):
    from mwclient import  Site
    import  mwclient
    ua = 'MyCoolTool. Run by User:mayne. Using mwclient/' + mwclient.__ver__
    site = mwclient.Site(('http', 'gw2.huiji.wiki'),clients_useragent=ua,path='/')
    site.login('mayne','since2013')
    page = site.pages[word]
    page_text = page.text()[0:50]
    return  page_text



