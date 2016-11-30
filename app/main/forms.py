from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,TextAreaField,PasswordField,BooleanField
from wtforms.validators import Required,Length,Email
from flask.ext.pagedown.fields import PageDownField


class PostForm(Form):
    title = StringField('标题', validators=[Required()])
    tag = StringField('标签', validators=[Required()])
    content = PageDownField('内容', validators=[Required()])
    submit = SubmitField('Submit')

class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    password = PasswordField('密码',validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')
