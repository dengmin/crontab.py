
import datetime
from peewee import *
from manage import db

class Base(db.Model):
    gmt_create = DateTimeField(default=datetime.datetime.now)
    gmt_update = DateTimeField(default=datetime.datetime.now)

class User(Base):
    name = CharField()
    salt = CharField()
    password = CharField()
    realname = CharField()
    email = CharField()
    about_me = CharField()

class Job(Base):
    user = ForeignKeyField(User,related_name='jobs') #创建job的用户
    job_id = CharField(unique=True)
    job_name = CharField(unique=True)
    cron_type = IntegerField()
    cron_express = CharField()
    run_model = IntegerField(help_text='串行 并行')
    runas = CharField(help_text='跑任务的用户')
    timeout = IntegerField(help_text='任务超时时间')
    deleted = BooleanField(help_text='任务执行完成后是否删除')
    redo = BooleanField(help_text='任务运行失败是否重新执行')
    comment = CharField()

class Record(Base):
    job = ForeignKeyField(Job, related_name='records')
    return_code = IntegerField()
    message = TextField()
    pid = IntegerField()
    status = IntegerField()
    start_time = DateTimeField(default=datetime.datetime.now)
    end_time = DateTimeField()
