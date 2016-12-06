from app import create_app
from flask.ext.script import Manager, Shell
#from flask.ext.migrate import Migrate,MigrateCommand

app = create_app()
manager = Manager(app)
#migrate = Migrate(app,db)

#manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
#test1
#数据库更新操作
##1.创建迁移仓库 python manage.py db init(第一次需要)
##2.创建迁移脚本 python manage.py db migrate -m "initial migration"
##3.在对models.py做出修改之后，更新数据库 python manage.py db upgrade
